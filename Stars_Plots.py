import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import lightkurve as lk
from tqdm import tqdm

def star_png(color, smear_factor = 1.0, filename = 'test'):
    fig, ax = plt.subplots(figsize = (5,5))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.axis('off')
    t = np.linspace(0, 2*np.pi, 250)

    x = 3*np.sin(t)
    y = 3*np.cos(t)
    ax.fill(x, y, color =  color)

    x = 3.5*np.sin(t)
    y = 3.5*np.cos(t)
    ax.fill(x, y, color =  color, alpha = 0.5, edgecolor = 'None')

    x = 4*np.sin(t)
    y = 4*np.cos(t)
    ax.fill(x, y, color =  color, alpha = 0.2, edgecolor = 'None')
    length = 10

    x = np.linspace(-length, length, 50)
    y1 = [-k/length*smear_factor - smear_factor if k < 0 else k/length*smear_factor - smear_factor  for k in x  ]
    y2 = [k/length*smear_factor + smear_factor if k < 0 else -k/length*smear_factor + smear_factor  for k in x  ]
    ax.fill_between(x, y1 = y1, y2 = y2, color =  color)

    x = np.linspace(-smear_factor, smear_factor, 50)
    y1 = [-k*length/smear_factor - length if k < 0 else k*length/smear_factor  - length  for k in x  ]
    y2 = [k*length/smear_factor  + length if k < 0 else -k*length/smear_factor  + length  for k in x  ]
    ax.fill_between(x, y1 = y1, y2 = y2, color =  color, edgecolor = 'None')

    smear_factor = 2*smear_factor
    x = np.linspace(-length, length, 50)
    y1 = [-k / length * smear_factor - smear_factor if k < 0 else k / length * smear_factor - smear_factor for k in x]
    y2 = [k / length * smear_factor + smear_factor if k < 0 else -k / length * smear_factor + smear_factor for k in x]
    ax.fill_between(x, y1=y1, y2=y2, color=color, alpha = 0.5, edgecolor = 'None')

    x = np.linspace(-smear_factor, smear_factor, 50)
    y1 = [-k * length / smear_factor - length if k < 0 else k * length / smear_factor - length for k in x]
    y2 = [k * length / smear_factor + length if k < 0 else -k * length / smear_factor + length for k in x]
    ax.fill_between(x, y1=y1, y2=y2, color=color, alpha = 0.5, edgecolor = 'None')

    smear_factor = 2*smear_factor
    x = np.linspace(-length, length, 50)
    y1 = [-k / length * smear_factor - smear_factor if k < 0 else k / length * smear_factor - smear_factor for k in x]
    y2 = [k / length * smear_factor + smear_factor if k < 0 else -k / length * smear_factor + smear_factor for k in x]
    ax.fill_between(x, y1=y1, y2=y2, color=color, alpha = 0.2, edgecolor = 'None')

    x = np.linspace(-smear_factor, smear_factor, 50)
    y1 = [-k * length / smear_factor - length if k < 0 else k * length / smear_factor - length for k in x]
    y2 = [k * length / smear_factor + length if k < 0 else -k * length / smear_factor + length for k in x]
    ax.fill_between(x, y1=y1, y2=y2, color=color, alpha = 0.2, edgecolor = 'None')
    plt.tight_layout()
    plt.savefig('pictures/stars/'+ filename + 'png', transparent=True, bbox_inches = None)
    plt.close()

k_colors = [    '#ff7d24',  '#ff842d',  '#ff8a33',    '#ff9a41',    '#ffa548',  '#ffa548',  '#ffa448',    '#ffa349',    '#ffa24a','#ffa24c',    '#ffa24e',  '#ffa250',    '#ffa251',  '#ffa153', '#ffa256',    '#ffa158',  '#ffa25a',  '#ffa35e', '#ffa563',    '#ffa868',    '#ffac6f', '#ffb177',    '#ffb67f',  '#ffbc87',    '#ffc18f',  '#ffc797',  '#ffcc9f',    '#ffd1a7',   '#ffd6b0',  '#ffdab8',  '#ffdec0' , '#ffe1c7' , '#ffe5cf' ,'#ffe8d7' , '#ffebdf' , '#ffede6' ,'#ffefed' ,   '#fff2f6' ,'#fff4fe' , '#f3edff' , '#ebe7ff' , '#e4e3ff' , '#dddeff' , '#d7d9ff' ,'#d1d6ff' , '#ccd2ff' , '#c7cfff' , '#c2cbff' , '#b8c5ff' ,'#b0bfff' , '#abbcff' , '#a2b5ff' ,'#9ab0ff' ,'#93aaff' , '#8da6ff' , '#8ba4ff' , '#87a1ff' , '#849fff' , '#819dff' , '#7f9bff' ,'#7d99ff' , '#7b97ff' , '#7996ff' ,    '#7895ff' ,    '#7794ff' ,  '#7693ff' ,  '#7592ff' ,  '#7491ff' , '#7391ff' ,  '#7290ff' , '#7290ff' ,  '#728fff' ,  '#718fff' , '#708eff' ,  '#6f8dff' , '#6e8cff' ,  '#6d8bff' ,  '#6c8aff' ,  '#6b89ff' ,  '#6988ff' ,  '#6887ff',   '#6686ff',   '#6585ff','#6484ff','#6383ff', '#6283ff',   '#6182ff',   '#6181ff',   '#6081ff', '#5f80ff', '#5f80ff', '#5e7fff', '#5e7fff',   '#5d7fff',   '#5d7eff',   '#5c7dff', '#5b7cff', '#5b7cff', '#5b7bff', '#5a7bff', '#5a7bff', '#5b7bff', '#5b7bff', '#5b7cff', '#5c7cff',]
k_temps = [     2300 ,   2400 ,   2500 ,     2600 ,     2700 ,   2800 ,   2900 ,     3000 , 3100 ,3200,     3300 ,   3400 ,     3500 ,   3600 , 3700,     3800 ,   3900 ,   4000 , 4100,     4200 ,     4300 ,4400,     4500 ,   4600 ,     4700 ,   4800 ,   4900 ,     5000 ,    5100,   5200 ,  5300 , 5400 , 5500 , 5600, 5700 , 5800 , 5900, 6000 , 6100, 6200 , 6300 , 6400 , 6500 , 6600 , 6700, 6800 , 6900 , 7000 , 7200 , 7400, 7600 , 7800 , 8000, 8200, 8400 , 8600 , 8800 , 9000 , 9200 , 9400 , 9600, 9800 , 10000, 10200 , 10400 , 10600 , 10800 , 11000 , 11200, 11400 , 11600, 11800 , 12000 , 12500, 13000 , 13500, 14000 , 14500 , 15000 , 16000 , 17000 , 18000 , 19000 , 20000, 21000, 22000 , 23000 , 24000 , 25000 , 26000 , 27000 , 27500 , 28000, 29000 , 30000 , 32500 , 35000 , 37500 , 40000 , 42500 , 45000 , 47500 , 50000 , 52500 , 55000 ,]

def generate_star_pngs():
    for color, temp in zip(k_colors, k_temps):
        star_png(color, smear_factor=0.2, filename= str(temp))

def generate_stars_list():
    id = []
    teff = []
    xs = []
    ys = []
    size = []
    pulsator = []
    spot = []
    planet = []
    binary = []
    irregular = []
    planet_type = []
    planet_g = []
    planet_visited = []
    gas_hazard = []
    cold_hazard = []
    hot_hazard = []




    count = 1
    # s = np.random.lognormal(2, 1, 1000)
    s = np.random.uniform(0, len(k_temps), 1000)

    for star in s:
        star = int(star)
        if star >= len(k_temps):
            continue

        id.append(count)
        teff.append(k_temps[star])

        count = count + 1
        xs.append(np.random.uniform(-1000, 1000, 1)[0])
        ys.append(np.random.uniform(-1000, 1000, 1)[0])
        size.append(np.random.uniform(0, 10, 1)[0])

        if 6500 < k_temps[star] < 9000:
            if k_temps[star] < 7500:
                rand = np.random.randint(1, high =8)
                if rand <= 3:
                    pulsator.append(rand)
                else:
                    pulsator.append(0)
            else:
                rand = np.random.uniform(1, 10, 1)[0]
                if rand < 5:
                    pulsator.append(2) # 1 means gmodes, 2 means delta cuti, 3 means hybrid
                else:
                    pulsator.append(0)
        elif 11000 <= k_temps[star] <= 25000:
            rand = np.random.uniform(1, 10, 1)[0]
            if rand < 5:
                pulsator.append(1) # SPB Beta Ceph
            else:
                pulsator.append(0)
        else:
            pulsator.append(0)


        rand = np.random.uniform(1, 10, 1)[0]
        if  k_temps[star] < 5000:
            if rand < 5:
                spot.append(1) # 1 means spot, 0 means no spot
            else:
                spot.append(0)
        elif  k_temps[star] < 10000:
            if rand < 3:
                spot.append(1) # 1 means spot, 0 means no spot
            else:
                spot.append(0)
        else:
            if rand == 1:
                spot.append(1) # 1 means spot, 0 means no spot
            else:
                spot.append(0)

        rand = np.random.uniform(1, 10, 1)[0]
        if rand <2:
            planet.append(rand) # 1 means planet, 0 means no planet
            planet_type.append(np.random.randint(1, high = 6))
            planet_g.append(np.random.uniform(2, 100, 1)[0]/9.81)
            planet_visited.append(0)
            gas = np.random.randint(1, high=6)
            if gas ==1:
                gas_hazard.append(gas)
            else:
                gas_hazard.append(0)

            gas = np.random.randint(1, high=11)
            if gas < 5:
                gas2 = np.random.randint(1, high=4)
                if gas2 == 1:
                    cold_hazard.append(1)
                    hot_hazard.append(0)
                else:
                    cold_hazard.append(0)
                    hot_hazard.append(1)
            else:

                cold_hazard.append(0)
                hot_hazard.append(0)

        else:
            planet.append(0)
            planet_type.append(0)
            planet_g.append(0)
            planet_visited.append(0)
            gas_hazard.append(0)
            cold_hazard.append(0)
            hot_hazard.append(0)




        rand = np.random.uniform(1, 20, 1)[0]
        if rand <2:
            binary.append(rand) # 1 means eclipsing binary, 0 means no eclipsing binary
        else:
            binary.append(0)




        rand = np.random.uniform(1, 15, 1)[0]
        if rand ==1:
            irregular.append(rand) # 1 means eclipsing binary, 0 means no eclipsing binary
        else:
            irregular.append(0)


    np.savetxt('stars_list.txt', np.array([id, teff, xs, ys, size, pulsator, spot, planet, binary, irregular, planet_type, planet_g, planet_visited, gas_hazard, cold_hazard, hot_hazard]).T, fmt = '%i')

def sin(x: np.ndarray, amp: float, f: float, phase: float) -> np.ndarray:
    """
    Sinus function, used for fitting.

    :param x: Time axis, days
    :param amp: amplitude, mag
    :param f: frequency, c/d
    :param phase: phase, normed to 1
    """
    return amp * np.sin(2. * np.pi * (f * x + phase))

def generate_star_lcs():
    data = np.loadtxt('stars_list.txt')
    for star in tqdm(data):
        # print(star)
        times = np.linspace(0, 50, 8000)
        flux = np.ones(len(times))
        # print('')
        if star[5] == 1 or star[5] ==3:
            # print('add gmodes')
            num_fs = np.random.uniform(3, 10)
            fs = np.random.uniform(1, 5, int(num_fs))
            amps = np.random.uniform(0.0005, 0.002, int(num_fs))
            phis = np.random.uniform(0, 1, int(num_fs))
            for f, a, p in zip(fs, amps, phis):
                flux += sin(times, a, f, p)

        if star[5] == 2 or star[5] ==3:
            # print('add pmodes')
            num_fs = np.random.uniform(5, 10)
            fs = np.random.uniform(30, 50, int(num_fs))
            amps = np.random.uniform(0.005, 0.02, int(num_fs))
            phis = np.random.uniform(0, 1, int(num_fs))
            for f, a, p in zip(fs, amps, phis):
                flux += sin(times, a, f, p)

        if star[6] ==1:
            # print('add spot')
            num_spots = np.random.randint(1, high = 4)
            if num_spots == 1:
                which = np.random.randint(0, high = 30)
                blueprint = np.loadtxt(f'Ksint/data/1_spot_{which}.txt').T
            elif num_spots == 2:
                which = np.random.randint(0, high = 50)
                blueprint = np.loadtxt(f'Ksint/data/2_spot_{which}.txt').T
            else:
                which = np.random.randint(0, high = 20)
                blueprint = np.loadtxt(f'Ksint/data/3_spot_{which}.txt').T
            period = np.random.uniform(1, 5)
            spot = interp1d(blueprint[0]*10, blueprint[1], fill_value = 'extrapolate')

            # print(np.min(blueprint[0]), np.max(blueprint[0]), np.min(times%blueprint[0][-1]), np.max(times%blueprint[0][-1]))
            flux = flux*spot(times%(blueprint[0][-1]*10) )

        if star[7] == 1:
            # print('add planet')
            # which = np.random.randint(0, high = 20)
            blueprint = np.loadtxt(f'Ksint/data/planet.txt').T
            random_stretch = np.random.uniform(0.5, 1.5, 1)[0]
            time = blueprint[0] * random_stretch
            random_squeeze = np.random.uniform(0.5, 1.5, 1)[0]
            flux_planet = (blueprint[1] - 1) * random_squeeze + 1
            planet = interp1d(time, flux_planet, fill_value = 'extrapolate')
            flux = flux*planet(times%time[-1])

        if star[8] == 1:
            # print('add binary')
            which = np.random.randint(0, high = 50)
            blueprint = np.loadtxt(f'Ksint/data/binary_{which}.txt').T
            binary = interp1d(blueprint[0], blueprint[1], fill_value = 'extrapolate')
            flux = flux*binary(times%blueprint[0][-1])

        flux += np.random.normal(0, 0.001, len(times))
        fig, ax = plt.subplots(figsize = (10,6))
        # pdg = lk.LightCurve(times, flux).to_periodogram()
        ax.plot(times, flux, 'ko', ms = 0.7)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Helligkeit')
        ax.set_xlim(0, 50)
        plt.tight_layout()
        plt.savefig(f'pictures/stars/PIC_{int(star[0])}_full.png')
        plt.close()

        fig, ax = plt.subplots(figsize = (10,6), dpi = 100)

        min = np.argmin(flux)
        if times[min] < 5:
            min = 5
        elif times[min] > 45:
            min = 45
        else:
            min = times[min]
        ax.plot(times, flux, 'ko', ms = 0.7)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Helligkeit')
        ax.set_xlim(min - 5, min + 5)
        plt.tight_layout()
        plt.savefig(f'pictures/stars/PIC_{int(star[0])}_days.png')
        plt.close()

        fig, ax = plt.subplots(figsize = (10, 6))

        min = np.argmin(flux)
        if times[min] < 0.25:
            min = 0.25
        elif times[min] > 49.75:
            min = 49.75
        else:
            min = times[min]
        ax.plot(times, flux, 'ko', ms=2)
        ax.set_xlabel('Zeit')
        ax.set_ylabel('Helligkeit')
        ax.set_xlim(min - 0.25, min + 0.25)
        plt.tight_layout()
        plt.savefig(f'pictures/stars/PIC_{int(star[0])}_hours.png')
        plt.close()

generate_stars_list()
generate_star_lcs()

#
# plt.hist(s,bins = 100)
# plt.plot([len(k_temps),len(k_temps)] , [0, 1000], 'r-')
# plt.show()
# print(s)
