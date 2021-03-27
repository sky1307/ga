import random
import yaml
from ga.Population import Population


class GA:
    with open("settings/ga/setting.yaml", 'r') as stream:
        config =yaml.load(stream ,Loader=  yaml.FullLoader)
    SIZE_POPULATION = config['SIZE_POPULATION']
    CONDITION_STOP =  config['CONDITION_STOP'] 
    pc = config['pc']
    pm = config['pm']
    def __init__(self , sigma ,  fitness):
        f0 = open("log/ga/init.txt", 'a+')
        f0.write("Hello")
        f0.close()
        print("hello>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
        self.pop = Population(size = GA.SIZE_POPULATION, sigma = sigma,f = fitness)
     
        print("--------------------close----------------------------")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        print("-")
        

    def crossover_mutation(self):
        a = random.randint(0, GA.SIZE_POPULATION -1 )
        b = random.randint(0, GA.SIZE_POPULATION -1 )
        while a == b:
            b = random.randint(0, GA.SIZE_POPULATION -1)
        ind1 = self.pop.pop[a]
        ind2 = self.pop.pop[b]
        p = random.random()
        if p < GA.pc:
            return self.pop.crossover(ind1,ind2)
        else:
            return self.pop.mutation(ind1) + self.pop.mutation(ind2)

    def run(self):
       
        i = 0
        while i < GA.CONDITION_STOP:
            child = []
            while len(child) < GA.SIZE_POPULATION:
                       child += self.crossover_mutation()
            self.pop.pop += child
            print(self.pop.get_best())
            self.pop.selection()
            
            for x in self.pop:
                x.write_file("log/ga/hientai.txt",'w+')

            f2 = open("log/ga/runtime.txt","a+")
            f2.seek(0,2)
            print("\n+++++++++++++++Chon loc lan thu : ",i+1,"+++++++++++++++++++\n")
            f2.write("\n+++++++++++++++Chon loc lan thu : "+str(i+1)+"+++++++++++++++++++\n")
            print("+")
            print("+")
            print("+")
            f1 = open("log/ga/run.txt", 'a+')
            f1.seek(0,2)
            f1.write("\n----------------the he: "+str(i+1)+"--------------\n")
            for i in range(GA.SIZE_POPULATION):
                f1.write(self.pop.pop[i].__str__())
                f1.write("\n")
            i +=1
            f1.close()
            f2.write("\n+++++++++++++++Chon  loc  xong : "+str(i+1)+"+++++++++++++++++++\n")
            print("-----------------------------------------------------")
            f2.close()
        return self.pop.get_best()    

