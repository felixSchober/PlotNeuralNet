
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
	to_input( 'input.png', to='(-4, 0, 8)'),


	to_Conv(name='embedding', offset="(0,0,10)", to="(0,0,0)", x_label=8000, z_label=300, width=2, height=30, depth=60, caption='Embedding', fillColor='\GreenColor' ),

	# encoder
	*attention_head('ath1', 1, offset="(4,0,0)"),
	*attention_head('ath2', 2, offset="(4,0,10)"),
	*attention_head('ath3', 3, offset="(4,0,20)"),

	#to_Conv(name='ath1', offset="(4,0,0)", x_label=64, z_label=64, width=2, height=24, depth=24, caption='Attention Head 1' ),
	# to_Conv(name='ath2', offset="(4,0,10)", x_label=64, z_label=64, width=2, height=24, depth=24, caption='Attention Head 2' ),
	# to_Conv(name='ath3', offset="(4,0,20)", x_label=64, z_label=64, width=2, height=24, depth=24, caption='Attention Head 3' ),
	
	
	to_intermediate_connection("embedding", "ath1_s", points_between=[('(2,0,10)', ''), ('(2,0,0)', '')]),    
	to_connection("embedding", "ath2_s"),
	to_intermediate_connection("embedding", "ath3_s", points_between=[('(2,0,10)', ''), ('(2,0,20)', '')]),    


	to_ball("concat1", offset="(9, 0, 10)"),

	to_connection("ath2_e", "concat1"),

	to_intermediate_connection("ath1_e", "concat1", points_between=[('(8,0,0)', '\midarrow'), ('(8,0,10)', '')]),    
	to_intermediate_connection("ath3_e", "concat1", points_between=[('(8,0,20)', ''), ('(8,0,10)', '\midarrow')]),    

	to_Pool(name="drp1", offset="(10.3,0,10)", opacity=0.5, width=1, height=24, depth=24, caption='Dropout'),

	to_connection("concat1", "drp1"),    

	to_ball("concat2", offset="(12, 0, 10)"),

	to_connection("drp1", "concat2"),    
	to_intermediate_connection("embedding", "concat2", points_between=[('(0.15,8,10)', '\midarrow'), ('(12,8,10)', '\midarrow')], of_direction='north', to_direction='north'),    

	to_ConvRes(name='layerNorm', offset="(14,0,10)", s_filer='', n_filer='', width=2, height=24, depth=24, caption='Layer Norm' ),

	to_connection("concat2", "layerNorm"),    

	to_ConvConvRelu(name='pwfw', offset="(17,0,10)", s_filer=300, n_filer=[300, 300], to="(0,0,0)", width=(4,4), height=24, depth=24, caption='PW Feed Forward' ),

	to_connection("layerNorm", "pwfw"),    

	to_Pool(name="drp2", offset="(19,0,10)", opacity=0.5, width=1, height=24, depth=24),

	to_ball("concat3", offset="(21.5, 0, 10)"),

	to_connection("drp2", "concat3"),    
	to_intermediate_connection("layerNorm", "concat3", points_between=[('(15.5,0,10)', ''), ('(15.5,8,10)', ''), ('(21.5,8,10)', '\midarrow')], of_direction='east', to_direction='north'),    

	
	to_Conv(name='asp1', offset="(25,0,5)", width=3, height=24, depth=24, caption='Aspect Price' ),
	to_Conv(name='asp2', offset="(25,0,15)", width=3, height=24, depth=24, caption='Aspect Quality' ),
	to_SoftMax(name='sm1', offset="(25.7,0,5)", width=1, height=3, depth=24, z_label=4),
	to_SoftMax(name='sm2', offset="(25.7,0,15)", width=1, height=3, depth=24, z_label=4),
     
	to_intermediate_connection("concat3", "asp1", points_between=[('(23.5,0,10)', ''), ('(23.5,0,5)', '')]),    
	to_intermediate_connection("concat3", "asp2", points_between=[('(23.5,0,10)', ''), ('(23.5,0,15)', '')]),    

    to_end() 
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
