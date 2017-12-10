import sys
import os

class Light:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    def distance(self, _x, _y):
        return (self.x - _x)**2 + (self.y - _y)**2
    def direction(self, _x, _y):
        X = abs(self.x - _x)
        Y = abs(self.y - _y)
        if Y > X:
            if self.y < _y:
                return "a"
            else:
                return "b"
        else:
            if self.x  > _x:
                return "c"
            else:
                return "d"
            
light_list = []
light_list.append(Light(521677,58109))
light_list.append(Light(521580,57466))
light_list.append(Light(521520,57059))
light_list.append(Light(521452,56668))
light_list.append(Light(521433,55855))
light_list.append(Light(521411,54822))
light_list.append(Light(521400,53998))


folderPath = os.path.dirname(os.path.realpath(__file__)) + "\day"
print folderPath
fileList = os.listdir(folderPath)
for fileName in fileList:
    if "0505.txt" in fileName:
        print folderPath+"\\"+fileName
        file = open(folderPath+"\\"+fileName)
        car_line_dict = {}
        lines = file.readlines()
        for line in lines:
            car = line.split(",")[0]
            if car_line_dict.has_key(car):
                car_line_dict[car].append(line)
            else:
                tmp_list = []
                tmp_list.append(line)
                car_line_dict[car] = tmp_list
        for aLight in light_list:
            print aLight.x,aLight.y
            lightIndex = light_list.index(aLight)
            fileName = fileName.replace(".txt","")
            print folderPath+"\\"+fileName+"out"+str(lightIndex)
            fileOut = open(folderPath+"\\"+fileName+"out"+str(lightIndex),"w")
            for car,_lines in car_line_dict.items():
                carxb,caryb,timeb = 0,0,0
                for line in _lines:
                    splitList = line.split(",")
                    if _lines.index(line)==0:
                        carxb = float(splitList[2])
                        caryb = float(splitList[3])
                        timeb = int(splitList[1])
                    carx = float(splitList[2])
                    cary = float(splitList[3])
                    time = int(splitList[1])
                    if aLight.direction(carxb,caryb)!=aLight.direction(carx,cary) and time-timeb<=4:
                        # print str(time) + "\t" + str(timeb)
                        output = splitList[0] +"\t"+ splitList[1]+"\t"+str(lightIndex) +"\t"+aLight.direction(carxb,caryb)+aLight.direction(carx,cary)+"\n"
                        fileOut.write(output)
                    carxb = carx
                    caryb = cary 
                    timeb = time
            fileOut.close