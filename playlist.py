import discord
from discord.ext import commands

import pandas as pd

class Playlist():

    def __init__(mode, p_time = 60.0):
        self.mode = mode
        self.start_intensity = 5
        self.end_intensity = 0
        self.p_time = p_time
        self.falloff = Falloff.linear

    #add a mode param function

    def load(pl_path, mode = 'sleep', curve = 'linear'):
        p_list = pd.read_csv(pl_path)

        if mode == 'sleep':
            self.n_songs = int(p_time / 2.5)  #change this to be mode dependent 
        #change this to be mode dependent 

        q = []

        for i in range(n_songs):
            progress = i/n_songs
            inty = self.falloff(self.start_intensity, self.end_intensity, progress)
            sp = p_list[p_list.Intensity == inty].sample(1)
            q.append(sp.values[0][0] + sp.values[0][1])
        
        self.queue = q



class Falloff():

    def linear(start_intensity, end_intensity, progress = 0.0):
        return int((start_intensity - end_intensity)*(1 - progress))