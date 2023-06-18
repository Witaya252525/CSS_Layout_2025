import pygame
import pygame_widgets

#init GUI
pygame.init()
screen = pygame.display.set_mode((1000,600))
done = False

#light
labelLight = pygame_widgets.TextBox(
    screen,
    470, 20,
    200, 50,
    fontSize = 30,
    textColour = (255,255,255),
    colour = (0,0,0))
sliderLight = pygame_widgets.Slider(
    screen,
    100,100,
    800, 20,
    min = 0, max = 100,
    step = 1,
    handleRadius = 30,
    handleColour = ((252,244,3)) )
labelValueLight = pygame_widgets.TextBox(
    screen,
    475, 150,
    80, 50,
    fontSize = 30,
    textColour = (255,255,255),
    colour = (0,0,0))
labelLED = pygame_widgets.TextBox(
    screen,
    455, 200,
    100, 50,
    fontSize = 30,
    textColour = (207,206,194),
    colour = (0,0,0) )

#moisture
labelMoisture = pygame_widgets.TextBox(
    screen,
    450, 320,
    200, 50,
    fontSize = 30,
    textColour = (255,255,255),
    colour = (0,0,0))
sliderMoisture = pygame_widgets.Slider(
    screen,
    100,400,
    800, 20,
    min = 0, max = 100,
    step = 1,
    handleRadius = 30,
    handleColour = ((0,238,242)) )
labelValueMoisture = pygame_widgets.TextBox(
    screen,
    475, 450,
    80, 50,
    fontSize = 30,
    textColour = (255,255,255),
    colour = (0,0,0))
labelPump = pygame_widgets.TextBox(
    screen,
    455, 500,
    100, 50,
    fontSize = 30,
    textColour = (207,206,194),
    colour = (0,0,0) )

#setting
setting = {
    "light" : 50,
    "moisture" : 80
    }

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
    #light
    labelLight.setText("Light")
    labelLight.draw()
    
    sliderLight.listen(events)
    lightValue = sliderLight.getValue()
    sliderLight.draw()
    
    labelValueLight.setText(lightValue)
    labelValueLight.draw()
    
    if(lightValue < setting["light"]):
        labelLED.setText("LED ON")
        labelLED.textColour = ((252,244,3))
    else:
        labelLED.setText("LED OFF")
        labelLED.textColour = ((207,206,194))
    labelLED.draw()
    
    #moisture
    labelMoisture.setText("Moisture")
    labelMoisture.draw()
    
    sliderMoisture.listen(events)
    moistureValue = sliderMoisture.getValue()
    sliderMoisture.draw()
    
    labelValueMoisture.setText(moistureValue)
    labelValueMoisture.draw()
    
    if(moistureValue < setting["moisture"]):
        labelPump.setText("Pump ON")
        labelPump.textColour = ((0,38,242))
    else:
        labelPump.setText("Pump OFF")
        labelPump.textColour = ((207,206,194))
    labelPump.draw()
    
    pygame.display.update()
    screen.fill((0,0,0))