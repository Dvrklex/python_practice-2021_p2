series = [
    ["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 5],
    ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]
    ]
pelis = [
    ["Inception", 4760183, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
    ["Batman Begins", 17319533, 'Christian Bale,Cillian Murphy,Michael Caine', 140],                 
    ["Inmortales", 35, 'Mirtha Legrand,Leonardo DiCaprio,Elizabeth The Second', 30]
    ]

actors = {}


for i in range(len(pelis)):
    # print(pelis[i][2])
    if i <= 1:  
          
        # print(pelis[i][2],'---cantidad de actores',len(pelis[i][2].split(',')))
        # print(series[i][2],'---cantidad de actores',len(series[i][2].split(',')))
        actorSer = series[i][2].split(',')
        # actorPel = pelis[i][2].split(',')
        # print(actorPel)
        # print(actorSer)
        for ser in actorSer:                    
            print(ser)
            if ser not in pelis[i][2]:
                pass
            else: 
                print('aca entro al if')
                
            # else:                       
            #     actors[ser] += 1
            # if pel not in actors.keys():
            #     actors[pel] = 1
            # else:                       
            #     actors[pel] += 1
    else:
        pass
        # actorPel = pelis[i][2].split(',')
        # for e in actorPel:
        #     if e not in actors.keys():
        #         actors[e] = 1
        #     else:                       
        #         actors[e] += 1
        # print(pelis[i][2],'---',len(pelis[i][2].split(',')))
