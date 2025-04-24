class converter:
        def convert_length(self,len, from_unit, to_unit):
            len_in_meters=0
            converted_len=0
            conversion_factors_height = {
                'meters': 1,
                'kilometers': 0.001,
                'centimeters': 100,
                'millimeters': 1000,
                'miles': 0.000621371,
                'yards': 1.09361,
                'feet': 3.28084,
                'inches': 39.3701
            }

            len_in_meters = len / conversion_factors_height[from_unit]
            converted_len = len_in_meters * conversion_factors_height[to_unit]
            print(converted_len ,"in",to_unit)

from_unit=input("Enter the unit for length: ")
to_unit=input("Enter the unit to which u want to convert: ")
len=float(input("Enter the length: "))
result=converter()
result.convert_length(len,from_unit,to_unit)



