city_info = 'Kabul, (1), "", " ", chen, 33°N, 65°E, ﻿ / ﻿, 33°N 65°E, ﻿ /, 33; 65, \
    Coordinates, :, 33°N, 65°E, ﻿ / ﻿, 33°N 65°E, ﻿ /, 33; 65'


city_info = [x.strip() for x in city_info.split(',')]
new_city_info = []
print(city_info)
new_city_info = [x for x in city_info[1:] if x[0].isdigit()]
new_city_info.insert(0, city_info[0])
print(new_city_info)
