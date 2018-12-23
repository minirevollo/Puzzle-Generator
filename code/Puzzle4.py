# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 14:59:30 2018

@author: Andreas Reheis
member of the erfindergarden
"""

from random import randint 
from tkinter import *
from time import *



class PUZZLE:
    
    def __init__(self, reihen, zeilen):
        ###Initialisiert das Puzzle.###
        self.svg = 0 
        self.name = "Puzzle_Version_4.svg"
        self.raster_x = 80
        self.raster_y = 80
        self.zeilen = reihen
        self.reihen = zeilen
        self.breite = self.raster_x * self.reihen
        self.hoehe =self.raster_y * self.zeilen
        self.dokumenten_anfang = "<?xml version=\"1.1\" encoding=\"UTF-8\"?>" + "\n"\
                                   + "<svg" + "\n"\
                                   + "xmlns = \"http://www.w3.org/2000/svg\"" + "\n" \

        self.dokumenten_breite = "width = \"" + str(self.breite) + "\""
        self.dokumenten_hoehe = "height = \"" + str(self.hoehe) + "\""
        self.dokumenten_viewbox = "viewBox= \"0 0 " + str(self.breite) + " " + str(self.hoehe) + "\">\n"
        self.pfad_nr = 0
        self.dokumenten_ende = "</svg>"    
    
    def schreiben_einleitung(self):
        ###Erzeugt eine neue Datei und schreibt die Dokumenteneinstellungen.###
        
       self.svg = open(self.name, "w")
       self.svg.write(self.dokumenten_anfang + "\n")
       self.svg.write(self.dokumenten_breite + "\n")
       self.svg.write(self.dokumenten_hoehe + "\n")
       self.svg.write(self.dokumenten_viewbox + "\n")
       self.svg.close()
    
    def zeilen_erstellen(self):
        ###Erstellt für die Zeilen einen Teilpfad nach dem anderen und fügt ihn der Datei hinzu.###
        
        ###Öffnen der Datei.###
        self.svg = open(self.name, "a")
        ###Position x wird auf 0 gesetzt. 
        
        for zeile in range(1, self.zeilen):
            ausrichtung = [-1, 1]
            p1x = 0
            p1y = zeile * self.raster_y
            self.pfad_anfang()
            self.svg.write(" d=\"M " + str(p1x) + "," + str(p1y) + " " + "C")
            for reihe in range(self.reihen):
                dir = ausrichtung[randint(0, 1)]
                c1x = p1x + 10
                c1y = p1y + randint(-2, 2)
                self.svg.write(str(c1x) + "," + str(c1y) + " ")
                c2x = p1x + randint(25, 29)
                c2y = p1y + randint(6, 10) * dir
                self.svg.write(str(c2x) + "," + str(c2y) + " ")
                p2x = p1x + randint(28, 33) 
                p2y = p1y + randint(-2, 2)
                self.svg.write(str(p2x) + "," + str(p2y) + " ")
                c3x = p1x +  randint(13, 15)
                c3y = p2y - randint(20, 26) * dir
                self.svg.write(str(c3x) + "," + str(c3y) + " ")
                c4x = p1x + randint(56, 63)
                c4y = p2y - randint(20, 26) * dir
                self.svg.write(str(c4x) + "," + str(c4y) + " ")
                p3x = p1x + randint(47, 52)
                p3y = p1y + randint(-2, 2)
                self.svg.write(str(p3x) + "," + str(p3y) + " ")
                c5x = p1x + randint(45, 50)
                c5y = p3y + randint(6, 10) * dir
                self.svg.write(str(c5x) + "," + str(c5y) + " ")
                c6x = p1x + self.raster_x - 10
                c6y = p1y + randint(-2, 2)
                self.svg.write(str(c6x) + "," + str(c6y) + " ")
                p4x = p1x + self.raster_x
                p4y = p1y
                self.svg.write(str(p4x) + "," + str(p4y) + " ")
                p1x = p4x
                p1y = p4y
            self.pfad_ende()
        self.svg.close()

    def reihen_erstellen(self):
        ###Erstellt für die Zeilen einen Teilpfad nach dem anderen und fügt ihn der Datei hinzu.###
        
        ###Öffnen der Datei.###
        self.svg = open(self.name, "a")
        ###Position x wird auf 0 gesetzt. 
                    
        for reihe in range(1, self.reihen):
            ausrichtung = [-2, 2]
            p1x = reihe * self.raster_x
            p1y = 0
            self.pfad_anfang()
            self.svg.write(" d=\"M " + str(p1x) + "," + str(p1y) + " " + "C")
            for zeile in range(self.zeilen):
                dir = ausrichtung[randint(0, 1)]
                c1x = p1x + randint(-2, 2)
                c1y = p1y + 10
                self.svg.write(str(c1x) + "," + str(c1y) + " ")
                c2x = p1x - randint(4, 8) * dir
                c2y = p1y + randint(26, 34)
                self.svg.write(str(c2x) + "," + str(c2y) + " ")
                p2x = p1x + randint(-2, 2) 
                p2y = p1y + randint(28, 32)
                self.svg.write(str(p2x) + "," + str(p2y) + " ")
                c3x = p2x + randint(10, 15) * dir
                c3y = 2 * p1y + 40 - c2y
                self.svg.write(str(c3x) + "," + str(c3y) + " ")
                c4x = p2x + randint(10, 15) * dir
                c4y = p1y + randint(60, 68)                
                self.svg.write(str(c4x) + "," + str(c4y) + " ")
                p3x = p1x
                p3y = p1y + randint(48, 52)                
                self.svg.write(str(p3x) + "," + str(p3y) + " ")
                c5x = p3x - randint(2, 8) * dir
                c5y = 2 * p1y + 110 - c4y                
                self.svg.write(str(c5x) + "," + str(c5y) + " ")
                c6x = p1x + randint(-2, 2)
                c6y = p1y + self.raster_y - 10             
                self.svg.write(str(c6x) + "," + str(c6y) + " ")
                p4x = p1x
                p4y = p1y + self.raster_y             
                self.svg.write(str(p4x) + "," + str(p4y) + " ")
                p1x = p4x
                p1y = p4y
            self.pfad_ende()        
        self.svg.close()
        
    def pfad_anfang(self):
        ###Schreibt den Anfang eines Pfades mit allen seinen Eigenschaften###
        
        self.svg.write("<path\n\t style=\"fill:none;stroke:#000000;stroke-width:0.50px;stroke-linecap:round;stroke-linejoin:miter;stroke-opacity:1\"\n")
        
         
    def pfad_ende(self):
        ###Schreibt das Ende des Pfades.###
        
        pfad_id = "pfad_" + str(self.pfad_nr)
        self.svg.write("\"" + "\n\tid=\"" + pfad_id  + "\" \n\tinkscape:connector-curvature=\"0\"\n />\n" + "\n")
        self.pfad_nr += 1
        
    def schreiben_ende(self):
        ###Schreibt das Ende der Datei.###
        
       self.svg = open(self.name, "a")
       self.svg.write(self.dokumenten_ende)
       self.svg.close()
       
    def rand_erstellen(self):
        ###Erstellt die Umrandung des Puzzles.###
        
        self.svg = open(self.name, "a")
        self.svg.write("<rect" + "\n"\
                        + "style=\"fill:none;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linejoin:round;stroke-miterlimit:4;"\
                        + "stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1\"" + "\n"\
                        + "id=\"Umrandung\"" + "\n"\
                        + "width=\"" + str(self.breite) + "\"" + "\n"\
                        + "height=\"" + str(self.hoehe) + "\"" + "\n"\
                        + "x=\"0\"" + "\n"\
                        + "y=\"0\"" + "\n"\
                        + "rx=\"1\"" + "\n"\
                        + "ry=\"1\" />" + "\n")
        self.svg.close()

    def text_erstellen(self):
            ###Erstellt das Branding auf dem Puzzle.###
            
            self.svg = open(self.name, "a")
            self.svg.write("<text xml:space=\"preserve\"" + "\n"\
                            + "style=\"font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-anchor:middle;font-size:15px;font-family:Consolas;writing-mode:lr-tb;fill:#ff0000;fill-opacity:1;stroke:none\"" + "\n"\
                            + "x=\"" + str(self.breite / 2) +"\"" + "\n"\
                            + "y=\"" + str(self.hoehe / 2) +"\"" + "\n"\
                            + "id=\"Branding\"" + "\n"\
                            + ">Puzzle Generator by mini revollo</text>" + "\n")
            self.svg.close()
    
    def ausgabebestaetigung(self):
        ### Feedback an den user.###
        
        print("\n Das Puzzle wurde in der Datei " + self.name + " abgespeichert\n und hat " + str(self.zeilen) + " x " + str(self.reihen) + " Teile" )
        
class FENSTER:
    ###Stellt alle Einstellungen für die erste Ansicht zur Verfügung.###
   
    def  __init__(self):
        ###Iniziert das Fenster.###
        
        print("Fenster  initiert")
        self.breite = 300
        self.hoehe = 300
        self.anzeige = Frame(root, bg = "black")
        self.anzeige.place(x = 0, y = 0, width = self.breite, height = self.hoehe)
        self.text_name = Label(text = "Puzzle Generator", font = ("Consolas", 20), fg = "green", bg = "black", anchor = "center")
        self.text_name.place(x = 0, y = 20, width = self.breite, height = 20)
        self.text_reihe = Label(text = "Spalten: ", fg = "green", bg = "black")
        self.text_zeile = Label(text = "Zeilen: ", fg = "green", bg = "black")
        self.text_reihe.place(x = 40, y = 60, width = 60, height = 20)
        self.text_zeile.place(x = 40, y = 80, width = 60, height = 20)
        self.input_reihe = Entry(self.anzeige, width = 3, bg = "silver", fg = "green")
        self.input_zeile = Entry(self.anzeige, width = 3, bg = "silver", fg = "green")
        self.input_reihe.insert(0, 16)
        self.input_zeile.insert(0, 12)        
        self.input_reihe.place(x = 140, y = 60)
        self.input_zeile.place(x = 140, y = 80)
        self.bt_erstellen = Button(self.anzeige, text="Puzzle erstellen", command = puzzle_erstellen)
        self.bt_erstellen.place(x = 100, y = 120, width = 100, height = 20)
        self.bt_beenden = Button(self.anzeige, text="beenden" , width=25, command=root.destroy)
        self.bt_beenden.place(x =100, y = 140, width = 100, height = 20)
        self.text_info = Label(text = "   by \n mini revollo \n  member of the \n erfindergarden", font = "Consolas", fg = "green", bg = "black", anchor = "center")
        self.text_info.place(x = 0, y = 180, width = self.breite, height = 80)
        self.text_ausgabe = Label(self.anzeige, text = "das Puzzle wurde gespeichert ", font = "Consolas", fg = "green", bg = "black", anchor = "center")
        
    def bestätigung(self, reihen, zeilen):
        ###Bestätigung der Puzzleabspeicherung.###
        
        ausgabetext = "das Puzzle wurde mit \n" + str(reihen) + " x " + str(zeilen) + " \n Teilen erstellt"
        self.text_ausgabe = Label(text = ausgabetext, font = "Consolas", fg = "green", bg = "black", anchor = "center")    
        self.text_ausgabe.place(x = 0, y = 180, width = self.breite, height = 80) 
         
def puzzle_erstellen():
    ###.Erstellt das Puzzle und speichert es ab.###
    puzzle = PUZZLE(int(fenster.input_zeile.get()),int(fenster.input_reihe.get()))
    puzzle.schreiben_einleitung()
    puzzle.zeilen_erstellen()
    puzzle.reihen_erstellen()
    puzzle.rand_erstellen()
    puzzle.text_erstellen()
    puzzle.schreiben_ende()
    fenster.bestätigung(puzzle.reihen, puzzle.zeilen)
                                                   
""" Setup """

root = Tk()         #ein Fenster erstellen
root.geometry("300x300")          #Größe zuordnen
root.title("           Puzzle Generator by mini revollo            ")
 #Fenster mit einem Titel versehen 
   
###Hier läuft das Programm ab.###    
fenster = FENSTER()

#root.after(0, puzzle_erstellen)    
root.mainloop()
 
       
        