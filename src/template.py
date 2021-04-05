"""
  한국 신호기 세트(Korean Signal Set)
  * Github repository      : https://github.com/KoreanGRF/KoreanSignalSet
"""

# Template for electric
template_electric = """
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
            replace({num2}, "./src/{gfx_code}/Y.real.png") {
                {template_name}()
            }
        } else {
            replace({num2}, "./src/{gfx_code}/Y.real.png") {
                {template_name}()
            }
        }
    } else {
        if(use_blue) {
            replace({num2}, "./src/{gfx_code}/Y.nonreal.png") {
                {template_name}()
            }
        } else {
            replace({num2}, "./src/{gfx_code}/Y.nonreal.png") {
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

# Template for semaphore
template_sempahore = """
// red
replace({num1}, "./src/{gfx_code}/R.png") {
    {template_name}()
}
// green
replace({num2}, "./src/{gfx_code}/G.png") {
    {template_name}()
}
"""

def signal_direction(tmpl, gfx_code, template_name, num1, num2):
    output = str(tmpl)
    output = output.replace('{num1}', str(num1))
    output = output.replace('{num2}', str(num2))
    output = output.replace('{gfx_code}', gfx_code)
    output = output.replace('{template_name}', template_name)
    return output

def replace_electric_signal(gfx_code, start_num):
    output = ""
    output = output + signal_direction(template_electric,  'electric/' + gfx_code, 'electric_signal_NE', start_num,    start_num+1)  + "\n"
    output = output + signal_direction(template_electric,  'electric/' + gfx_code, 'electric_signal_SW', start_num+2,  start_num+3)  + "\n"
    output = output + signal_direction(template_electric,  'electric/' + gfx_code, 'electric_signal_SE', start_num+4,  start_num+5)  + "\n"
    output = output + signal_direction(template_electric,  'electric/' + gfx_code, 'electric_signal_NW', start_num+6,  start_num+7)  + "\n"
    output = output + signal_direction(template_electric,  'electric/' + gfx_code, 'electric_signal_W',  start_num+8,  start_num+9)  + "\n"
    output = output + signal_direction(template_electric,  'electric/' + gfx_code, 'electric_signal_E',  start_num+10, start_num+11) + "\n"
    output = output + signal_direction(template_electric,  'electric/' + gfx_code, 'electric_signal_N',  start_num+12, start_num+13) + "\n"
    output = output + signal_direction(template_electric,  'electric/' + gfx_code, 'electric_signal_S',  start_num+14, start_num+15) + "\n"
    return output

def replace_semaphore_signal(gfx_code, start_num):
    output = ""
    output = output + signal_direction(template_sempahore, 'semaphore/' + gfx_code, 'semaphore_signal_NE', start_num,    start_num+1)  + "\n"
    output = output + signal_direction(template_sempahore, 'semaphore/' + gfx_code, 'semaphore_signal_SW', start_num+2,  start_num+3)  + "\n"
    output = output + signal_direction(template_sempahore, 'semaphore/' + gfx_code, 'semaphore_signal_SE', start_num+4,  start_num+5)  + "\n"
    output = output + signal_direction(template_sempahore, 'semaphore/' + gfx_code, 'semaphore_signal_NW', start_num+6,  start_num+7)  + "\n"
    output = output + signal_direction(template_sempahore, 'semaphore/' + gfx_code, 'semaphore_signal_W',  start_num+8,  start_num+9)  + "\n"
    output = output + signal_direction(template_sempahore, 'semaphore/' + gfx_code, 'semaphore_signal_E',  start_num+10, start_num+11) + "\n"
    output = output + signal_direction(template_sempahore, 'semaphore/' + gfx_code, 'semaphore_signal_N',  start_num+12, start_num+13) + "\n"
    output = output + signal_direction(template_sempahore, 'semaphore/' + gfx_code, 'semaphore_signal_S',  start_num+14, start_num+15) + "\n"
    return output
