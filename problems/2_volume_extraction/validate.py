from pedal import *


ensure_function('calculate_area', parameters=[float], returns=float)
ensure_function('calculate_volume', parameters=[float, float], returns=float)


cal_vol = find_function_definition("calculate_volume")
ensure_function_call('calculate_area', at_least=1, root=cal_vol)


ensure_function('calculate_area', at_least = 3)
ensure_function('calculate_volume', at_least = 3)


unit_test('calculate_area',
          ([0], 0),
          ([1], 3.14159),
          ([2], 12.56636)
          )

unit_test('calculate_volume',
          ([1, 2], 2*3.14159),
          ([5, 1], 78.53975),
          ([1, 0], 0)
          )


ensure_coverage(at_least=0.5)