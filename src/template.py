"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""

# Template
template = """
// red
if(is_realistic) {
    replace({num1}, "./src/{gfx_code}/R.real.png") {
        {template_name}()
    }
} else {
    replace({num1}, "./src/{gfx_code}/R.nonreal.png") {
        {template_name}()
    }
}

// green
if(use_caution_signal) {
	if(is_realistic) {
		if(use_blue) {
			replace({num2}, "./src/{gfx_code}/YB.real.png") {
				{template_name}()
			}
		} else {
			replace({num2}, "./src/{gfx_code}/YG.real.png") {
				{template_name}()
			}
		}
	} else {
		if(use_blue) {
			replace({num2}, "./src/{gfx_code}/YB.nonreal.png") {
				{template_name}()
			}
		} else {
			replace({num2}, "./src/{gfx_code}/YG.nonreal.png") {
				{template_name}()
			}
		}
	}
} else {
	if(is_realistic) {
		if(use_blue) {
			replace({num2}, "./src/{gfx_code}/B.real.png") {
				{template_name}()
			}
		} else {
			replace({num2}, "./src/{gfx_code}/G.real.png") {
				{template_name}()
			}
		}
	} else {
		if(use_blue) {
			replace({num2}, "./src/{gfx_code}/B.nonreal.png") {
				{template_name}()
			}
		} else {
			replace({num2}, "./src/{gfx_code}/G.nonreal.png") {
				{template_name}()
			}
		}
	}
}
"""

def add_signal_direction(gfx_code, template_name, num1, num2):
	output = str(template)
	output = output.replace('{num1}', str(num1))
	output = output.replace('{num2}', str(num2))
	output = output.replace('{gfx_code}', gfx_code)
	output = output.replace('{template_name}', template_name)
	return output