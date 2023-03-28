from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

class MainWindow(Screen):
    pass


class Tabel(BoxLayout):
    pass

class FCFS(Screen):
    def clicked_fcfs(self,pid,at,bt,ct_out,tat_out,wt_out):

        processes = []

        ct = [0] * len(pid)
        tat = [0] * len(pid)
        wt = [0] * len(pid)

        for i in range(len(pid)):
            processes.append([int(pid[i].text), int(at[i].text), int(bt[i].text)])
        print(processes)

        for j in range(len(processes)):
            ct[j] = processes[j][2] + ct[j - 1]  # Completion Time (less than cumulative frequency of processes)
            tat[j] = ct[j] - processes[j][1]  # Turn Around Time = Completion Time - Arrival Time
            wt[j] = tat[j] - processes[j][2]    #Waiting Time = Turnaround time - Burst Time
        (ct, tat, wt)
        for i in range(len(ct_out)):
            ct_out[i].text=str(ct[i])
            tat_out[i].text=str(tat[i])
            wt_out[i].text=str(wt[i])
        pass

class SJF(Screen):
    pass

class RR(Screen):
    pass

class Priority(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class OsTimeSchdulingAlgoApp(App):
    pass

if __name__=="__main__":
    OsTimeSchdulingAlgoApp().run()