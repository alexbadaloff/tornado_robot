# -*- coding=utf8 -*-
'''
Модуль представляет собой класс привод
'''
import threading,nxt
class Drive(threading.Thread):

    def __init__(self,Brick,PortOfDrive):
        threading.Thread.__init__(self) # создаем, но не запускаем поток
        self.brick=Brick
        self.PofDrv=PortOfDrive
        self.motor=nxt.Motor(self.brick,self.PofDrv)
        self.Start=False
    def SetParam(self,direction=1,power=100,degree=-1,block=0):
        '''
            direction - направление - принимает 2 значения +1 и -1
            + это положительное направление
            power - мощность вращения двигателя - по умолчанию 100%
            максимальное значение 127
            degree - угол поворота двигателя если  значение не  задано, то
            двигатель вращается до получения сигнала stop
            block - блокировка двигателя после окончания движения, 1 - блокирован, 0 - нет
            по умолчанию двигатель не блокируется
        '''

        self.direction=direction
        self.power=power
        self.degree=degree
        self.block=block
    def run(self):

        self.Start=True #Флаг начала работы
        self.NumOfRot=-1 # пока бесконечное число оборотов
        if self.degree==-1: # если угол не задан - вращаться бесконечно
            self.angle_of_rot=50 # задаем минимальный угол 50*
            self.NumOfRot=-1 #вращаемся бесконечно
        else:
            self.NumOfRot=self.degree//50
            if (self.degree % 50): # если количество поворотов не четное
                self.NumOfRot=self.NumOfRot+1 #то дополнительный поворот
            self.angle_of_rot=50 # и даем угол поворота 50*

        while self.NumOfRot: #до тех пор пока число поворотов не 0 (т.е. при -1 он будет вращаться всегда)
            if self.degree==-1: # если угол не задали
                self.NumOfRot=-1 # то вращаемся бесконечно
            else:
                if self.degree>=self.angle_of_rot: # если угол больше угла поворота
                    self.degree=self.degree-self.angle_of_rot # то уменьшаем значение угла
                else:
                    self.angle_of_rot=self.degree # если угол, заданный или оставшийся <50* - то попытаться повернуться на него

            self.motor.turn((self.power*self.direction),self.angle_of_rot,self.block) # поворачиваем вал на 50*
            if self.Start==False: # проверяем не пришла ли пора остановиться?
                break
            self.NumOfRot=self.NumOfRot-1
        pass
    def stop(self):
        self.Start=False #Флаг завершения процесса

