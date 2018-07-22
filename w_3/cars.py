#Gorohov Daniil uabeatifull

from os import path
import csv


class CarBase:
    def __init__(self,car_type, brand, photo_file_name, carrying = 0):
    	self.car_type = car_type
    	self.brand = brand  
    	self.photo_file_name = photo_file_name
    	self.carrying = float(carrying)

    
    def get_photo_file_ext(self):
    	try:
    		return path.splitext(self.photo_file_name)
    	except:
        	return ""

class Car(CarBase):
    def __init__(self,car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_width, body_height, body_length):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def get_body_volume(self):
    	return self.body_width*self.body_height*self.body_length
    
class SpecMachine(CarBase):
    def __init__(self,car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra
       

def get_car_list(csv_filename):
	car_list = []
	try:
		with open(csv_filename, encoding='utf-8') as csv_fd:
			reader = csv.reader(csv_fd, delimiter=';')
			next(reader)# пропускаем заголовок
			for row in reader:
				if 'car' in row:
					if len(row) >= 4:
						car = Car("car", row[1], row[3], row[5], row[2])
						car_list.append(car)

				elif 'truck' in row:
					if len(row) >= 4:
						if row[4]:
							xap = row[4].split('x')
						else:
							xap = [0 for _ in range(3)]

						truck = Truck("truck", row[1], row[3], row[5], float(xap[0]), float(xap[1]), float(xap[2]))
						car_list.append(truck)

				elif 'spec_machine' in row:
					if len(row) >=4:
						spec_machine = SpecMachine("spec_machine", row[1], row[3],row[5],row[6])
						car_list.append(spec_machine)

	except OSError as err:
		print("Coundn't reading the file!")
    
	return car_list



def main():
	tablecar = get_car_list("cars.csv")


if __name__ == '__main__':
	main()