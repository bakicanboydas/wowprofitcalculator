import random
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib import animation


def draw_graph(listOfIteration,listOfProfit):
	plt.scatter(listOfIteration,listOfProfit)
	plt.plot(listOfIteration,listOfProfit)
	plt.xlabel('Craft Number')
	plt.ylabel('Profit')
	plt.show()


def calculate(cost,rank2,rank3,inspiration,multicraft,avarageMulticraft,numberOfCraft,times10):
	total_price=0
	profit=0
	total_cost = cost * numberOfCraft
	numberOfInspirationProc = 0
	numberOfMulticraftProc = 0
	numberOfMulticraftProcWithInspirationProc = 0
	listOfProfit=[]
	listOfIteration=[]
	locationXlog = 1650
	locationYlog = 550
	locationXinfopopup = 600
	locationYinfopopup = 600
	if times10==True:
		for k in range(0,10):
			total_price = 0
			numberOfInspirationProc = 0
			numberOfMulticraftProc = 0
			numberOfMulticraftProcWithInspirationProc = 0
			listOfIteration.append(k+1)
			for i in range(0,numberOfCraft):
				if(random.randint(1,100)>inspiration):
					if(random.randint(1,100)>multicraft):
						total_price = total_price+rank2
						sg.Print("No proc",location=(locationXlog,locationYlog))
					else:
						total_price = total_price+(rank2*avarageMulticraft)
						numberOfMulticraftProc+=1
						sg.Print("Multicraft proc",location=(locationXlog,locationYlog))
				else:
					if(random.randint(1,100)>multicraft):
						total_price = total_price+rank3
						numberOfInspirationProc+=1
						sg.Print("Inspiration proc",location=(locationXlog,locationYlog))
					else:
						total_price = total_price+(rank3*avarageMulticraft)
						numberOfInspirationProc+=1
						numberOfMulticraftProc+=1
						numberOfMulticraftProcWithInspirationProc+=1
						sg.Print("Inspiration + Multicraft proc",location=(locationXlog,locationYlog))
			sg.Print("Crafting "+str(k+1)+" is over\n********************************************",location=(locationXlog,locationYlog))
			sg.popup_non_blocking("Total inspiration proc : " + str(numberOfInspirationProc) + "\n"
			+ "Total multicraft proc : " + str(numberOfMulticraftProc) + "\n"
			+ "Total multicarft proc when inspiration proc : " + str(numberOfMulticraftProcWithInspirationProc) + "\n"
			+ "Total Gold Receive : " + str(total_price) + "\n"
			+ "Total Cost : " + str(total_cost) + "\n"
			+ "Profit : " + str(total_price - total_cost),location=(locationXinfopopup,locationYinfopopup))
			listOfProfit.append(total_price - total_cost)
			sg.OneLineProgressMeter('Crafting...', numberOfCraft*(k+1), numberOfCraft*10,  'Wait for result please', 'Craft simulation contiune...')

		draw_graph(listOfIteration,listOfProfit)

	else:
		for k in range(0,100):
			total_price = 0
			numberOfInspirationProc = 0
			numberOfMulticraftProc = 0
			numberOfMulticraftProcWithInspirationProc = 0
			listOfIteration.append(k+1)
			for i in range(0,numberOfCraft):
				if(random.randint(1,100)>inspiration):
					if(random.randint(1,100)>multicraft):
						total_price = total_price+rank2
						sg.Print("No proc",location=(locationXlog,locationYlog))
					else:
						total_price = total_price+(rank2*avarageMulticraft)
						numberOfMulticraftProc+=1
						sg.Print("Multicraft proc",location=(locationXlog,locationYlog))
				else:
					if(random.randint(1,100)>multicraft):
						total_price = total_price+rank3
						numberOfInspirationProc+=1
						sg.Print("Inspiration proc",location=(locationXlog,locationYlog))
					else:
						total_price = total_price+(rank3*avarageMulticraft)
						numberOfInspirationProc+=1
						numberOfMulticraftProc+=1
						numberOfMulticraftProcWithInspirationProc+=1
						sg.Print("Inspiration + Multicraft proc",location=(locationXlog,locationYlog))
			sg.Print("Crafting "+str(k+1)+" is over\n********************************************",location=(locationXlog,locationYlog))
			sg.popup_non_blocking("Total inspiration proc : " + str(numberOfInspirationProc) + "\n"
			+ "Total multicraft proc : " + str(numberOfMulticraftProc) + "\n"
			+ "Total multicarft proc when inspiration proc : " + str(numberOfMulticraftProcWithInspirationProc) + "\n"
			+ "Total Gold Receive : " + str(total_price) + "\n"
			+ "Total Cost : " + str(total_cost) + "\n"
			+ "Profit : " + str(total_price - total_cost),location=(locationXinfopopup,locationYinfopopup))
			listOfProfit.append(total_price - total_cost)
			sg.OneLineProgressMeter('Crafting...', numberOfCraft*(k+1), numberOfCraft*100,  'Wait for result please', 'Craft simulation contiune...')

		draw_graph(listOfIteration,listOfProfit)
		
		


sg.theme('DarkAmber')

layout = [[sg.Text('Welcome to simple profit calculator!')],
         [sg.Text('Enter cost: 		'), sg.InputText()],
         [sg.Text('Enter rank2 price in AH: 	'), sg.InputText()],
         [sg.Text('Enter rank3 price in AH: 	'), sg.InputText()],
         [sg.Text('Enter your inspiration rate:    '), sg.InputText()],
         [sg.Text('Enter your multicraft rate: 	'), sg.InputText()],
         [sg.Text('Number of average multicraft:'), sg.InputText()],
         [sg.Text('Number of craft: 		'), sg.InputText()],
         [sg.Radio('Run 10 times simulation ', "times",default=True)],
         [sg.Radio('Run 100 times simulation ', "times")],
         [sg.Button('Ok'), sg.Button('Cancel')],
         [sg.Text('I recommend keeping the number of crafts low in 100 simulations. \nOtherwise it will take too long. If you have more crafts, use simulation 10 times.',text_color='red')]
]

window = sg.Window('DF Simple Profit Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    calculate(int(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4]),int(values[5]),int(values[6]),bool(values[7]))
    


window.close()