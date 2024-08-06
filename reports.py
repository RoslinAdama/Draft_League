import streamlit as st
import altair as alt
import pickle
import os
import numpy as np
import pandas as pd

from random import randint


st.set_page_config(layout='wide')



class Report():
    results : dict

    def __init__(self , results):
        self.results = results

    def hp_bar(hp , hp_max):
        dic = [hp,hp_max]
        return pd.DataFrame(dic)

    def phase_lane(self , num_phase):
        st.header("Phase lane")

        golds_mid_blue = self.results["golds"][0][num_phase]
        golds_mid_red = self.results["golds"][3][num_phase]

        golds_bot_blue = self.results["golds"][1][num_phase] + self.results["golds"][2][num_phase]
        golds_bot_red = self.results["golds"][4][num_phase] + self.results["golds"][5][num_phase]



        # pdb.set_trace()
        # golds_mid_blue = randint(600,999)
        # golds_mid_red = randint(600,999)

        # golds_bot_blue = randint(1300,1999)
        # golds_bot_red = randint(1300,1999)


        golds_total_blue = golds_mid_blue + golds_bot_blue
        golds_total_red = golds_mid_red + golds_bot_red



        diff = golds_total_blue - golds_total_red
        if diff >= 0:
            st.subheader(f"""Golds :blue[{golds_total_blue}] vs :red[{golds_total_red}]  (+:blue[{diff}])""")
        else:
            st.subheader(f"""Golds :blue[{golds_total_blue}] vs :red[{golds_total_red}]  (+:red[{abs(diff)}])""")

        diff_mid = golds_mid_blue - golds_mid_red
        if diff_mid >= 0:
            st.write(f"""Mid :blue[{golds_mid_blue}] vs :red[{golds_mid_red}]  (+:blue[{diff_mid}])""")
        else:
            st.write(f"""Mid :blue[{golds_mid_blue}] vs :red[{golds_mid_red}]  (+:red[{abs(diff_mid)}])""")

        diff_bot = golds_bot_blue - golds_bot_red
        if diff_bot >= 0:
            st.write(f"""Bot :blue[{golds_bot_blue}] vs :red[{golds_bot_red}]  (+:blue[{diff_bot}])""")
        else:
            st.write(f"""Bot :blue[{golds_bot_blue}] vs :red[{golds_bot_red}]  (+:red[{abs(diff_bot)}])""")



    def light_report(self):
        st.header("Winner : " + self.results["victoire"])
        st.text("Drake : " + self.results["drake"] + " " + self.results["drake type"])
        st.text("Baron : " + self.results["baron"])

    def drake(self):
        st.header("Drake")

        if self.results["drake"] == "Blue":
            st.subheader(f""":blue[Blue]""")
        else:
            st.subheader(f""":red[Red]""")

        degats = self.results["degats"][0]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        st.text("Dégâts infligés")
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)


        st.text("Dégâts tankés")
        degats = self.results["tanke"][0]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)

        st.text("Dégâts soignés")
        degats = self.results["heal"][0]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)





    def baron(self):
        st.header("Baron")
        if self.results["baron"] == "Blue":
            st.subheader(f""":blue[Blue]""")
        else:
            st.subheader(f""":red[Red]""")

        st.text("Dégâts infligés")
        degats = self.results["degats"][1]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)


        st.text("Dégâts tankés")
        degats = self.results["tanke"][1]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)

        st.text("Dégâts soignés")
        degats = self.results["heal"][1]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)

    def ancestral(self):
        st.header("Victoire")
        if self.results["victoire"] == "Blue":
            st.subheader(f""":blue[Blue]""")
        else:
            st.subheader(f""":red[Red]""")

        st.text("Dégâts infligés")
        degats = self.results["degats"][2]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)

        st.text("Dégâts tankés")
        degats = self.results["tanke"][2]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)

        st.text("Dégâts soignés")
        degats = self.results["heal"][2]
        damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})
        # st.write(self.results["degats"][0])
        # st.bar_chart(damage_data , x="noms" , y="damage" , color="color" )
        chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
        st.altair_chart(chart_df)


    def page_fights(self):
        cols = st.columns([5,3,5,3,4])
        with cols[0]:
            self.phase_lane(num_phase=0)

        with cols[1]:
            self.drake()

        with cols[2]:
            self.phase_lane(num_phase=2)

        with cols[3]:
            self.baron()

        with cols[4]:
            self.ancestral()





    # def page_resume(self):
    #     degats = self.results["degats"]
    #     degats_par_perso = {}
    #     for perso in degats[0].keys():
    #         degats_par_perso[perso] = 0

    #     for fight in range(3):
    #         for pers in degats[fight].keys():
    #             degats_par_perso[pers] += degats[fight][pers]

    #     st.write(degats_par_perso)
    #     degats = degats_par_perso.copy()

    #     damage_data = pd.DataFrame({"noms" : list(degats.keys())  , "damage" : list(degats.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})

    #     chart_df = alt.Chart(damage_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("damage" , sort=None) , color="color")
    #     st.altair_chart(chart_df)


    #     tankes = self.results["tanke"]
    #     tanks_par_perso = {}
    #     for perso in tankes[0].keys():
    #         tanks_par_perso[perso] = 0

    #     for fight in range(3):
    #         for pers in tankes[fight].keys():
    #             tanks_par_perso[pers] += tankes[fight][pers]

    #     st.write(tanks_par_perso)
    #     tankes = tanks_par_perso.copy()

    #     tankes_data = pd.DataFrame({"noms" : list(tankes.keys())  , "tankes" : list(tankes.values()) , "color" : ["Blue" , "Blue" , "Blue" , "Red" , "Red" , "Red"]})

    #     chart_df = alt.Chart(tankes_data).mark_bar().encode(x=alt.X("noms" , sort=None) , y=alt.Y("tankes" , sort=None) , color="color")
    #     st.altair_chart(chart_df)


    def simulation_game(self , num_fight):

        states = [st.session_state.state_drake , st.session_state.state_baron , st.session_state.state_ancestral]
        num_tour = states[num_fight]
        stats = self.results["save_fight"][num_fight]
        longueur_fight = len(stats)
        tour_engage = self.results["tour_engage"][num_fight]
        lvls = self.results["save_lvls"][num_fight]
        hp_max = self.results["hp_max"][num_fight]

        
        cols = st.columns([1,1,6,1,1])

        with cols[0]:

            if num_tour < tour_engage:

                for b,blue_champ in enumerate(self.results["blue_team"]):
                    st.subheader(lvls[0+b])
                    try:
                        st.image("data/images/"+blue_champ+".webp" , use_column_width=True)
                    except Exception:
                        st.image("data/images/"+blue_champ+".jpg" , use_column_width=True)
                    

            else:
                distances = stats[num_tour]["positions"]
                for b,blue_champ in enumerate(self.results["blue_team"]):
                    st.subheader(lvls[0+b])

                    if distances[b] is None:
                        st.image("data/images/dead/"+blue_champ+".jpg" , use_column_width=True)
                    else:
                        try:
                            st.image("data/images/"+blue_champ+".webp" , use_column_width=True)
                        except Exception:
                            st.image("data/images/"+blue_champ+".jpg" , use_column_width=True)



        with cols[1]:
            st.write("state : " , num_tour)

            # Pre fight
            if num_tour < tour_engage:
                # st.write(stats[0:2])


                if num_tour == -1:
                    pre_fight_hps = stats[0]["hps"]
                else:
                    pre_fight_hps = stats[num_tour]["hps"]

                dfs = [0]*3
                for i in range(3):
                    fight_hps = pre_fight_hps[i]
                    dfs[i] = pd.DataFrame({"hps" : [fight_hps,hp_max[i]]} , index=None)
                    st.write(fight_hps)
                    st.bar_chart(dfs[i] , height=180)
                    
                
            # Vrai fight
            elif num_tour  < longueur_fight - 1 :
                hps = stats[num_tour]["hps"]
                
                dfs = [0]*3
                for i in range(3):
                    fight_hps = hps[i]
                    dfs[i] = pd.DataFrame({"hps" : [fight_hps,hp_max[i]]} , index=None)
                    st.write(fight_hps)
                    st.bar_chart(dfs[i] , height=180)
            
            # Fight fini
            else:
                hps = stats[num_tour-1]["hps"]
                
                dfs = [0]*3
                for i in range(3):
                    fight_hps = hps[i]
                    dfs[i] = pd.DataFrame({"hps" : [fight_hps,hp_max[i]]} , index=None)
                    st.write(fight_hps)
                    st.bar_chart(dfs[i] , height=180)




        
        with cols[2]:

            # Boutons
            if num_tour == -1:
                if st.button("Commencer fight" , key=10+num_fight*7):
                    if num_fight == 0:
                        st.session_state.state_drake = 0
                    elif num_fight == 1:
                       st.session_state.state_baron = 0
                    else:
                        st.session_state.state_ancestral = 0

                    st.rerun()
                    

            elif num_tour < 101  and  num_tour < longueur_fight - 1:
                if st.button("Avancer",key=8+num_fight*11+99*num_tour):
                    if num_fight == 0:
                            st.session_state.state_drake += 1
                    elif num_fight == 1:
                        st.session_state.state_baron += 1
                    else:
                        st.session_state.state_ancestral += 1

                    st.rerun()

            if num_tour > 0:
                if st.button("Reculer",key=9+num_fight*11+99*num_tour):
                    if num_fight == 0:
                            st.session_state.state_drake -= 1
                    elif num_fight == 1:
                        st.session_state.state_baron -= 1
                    else:
                        st.session_state.state_ancestral -= 1

                    st.rerun()

                if st.button("Rénitialiser le fight" , key=200+13*num_fight):
                    if num_fight==0:
                        st.session_state.state_drake = - 1
                    elif num_fight == 1:
                        st.session_state.state_baron = - 1
                    else:
                        st.session_state.state_ancestral = - 1

                    st.rerun()
            
            if num_tour >= tour_engage:
                st.subheader("Engage par : " + self.results["perso_engage"][num_fight])
            else:
                st.subheader("Phase de poke")

            
            if num_tour >= tour_engage  and num_tour < longueur_fight - 1:
                st.write(stats[num_tour]["comments"])
                # st.write(stats[num_tour]["positions"])
                remplissage_cases = []
                for i in range(9):
                    remplissage_cases.append([])

                for i,b_perso in enumerate(self.results["blue_team"]):
                    dist = stats[num_tour]["positions"][i]
                    if dist is not None:
                        remplissage_cases[4-dist].append(b_perso)

                for i,r_perso in enumerate(self.results["red_team"]):
                    dist = stats[num_tour]["positions"][i+3]
                    if dist is not None:
                        remplissage_cases[4+dist].append(r_perso)

                for c,case in enumerate(remplissage_cases):
                    if c == 4:
                        st.subheader("Fight")

                    nb_persos = len(case)
                    if nb_persos > 0:
                        pos_cols = st.columns(nb_persos)

                        for p,perso in enumerate(case):
                            with pos_cols[p]:
                                try:
                                    nom_image = f"data/images/{perso}.webp"
                                    st.image(nom_image.format(perso),width=100)
                                except Exception as E:
                                    nom_image = f"data/images/{perso}.jpg"
                                    st.image(nom_image.format(perso),width=100)

                    st.divider()

            if num_tour >= longueur_fight - 1:

                if num_fight == 0:
                    self.drake()
                elif num_fight == 1:
                    self.baron()
                else:
                    self.ancestral()


            
                



        with cols[-2]:
            st.write("state : " , num_tour)

            # Pre fight
            if num_tour < tour_engage:
                if num_tour == -1:
                    pre_fight_hps = stats[0]["hps"]
                else:
                    pre_fight_hps = stats[num_tour]["hps"]

                dfs = [0]*3
                for i in range(3):
                    fight_hps = pre_fight_hps[i+3]
                    dfs[i] = pd.DataFrame({"hps" : [fight_hps,hp_max[i+3]]} , index=None)
                    st.write(fight_hps)
                    st.bar_chart(dfs[i] , height=180)
                    
                
            # Vrai fight
            elif num_tour  < longueur_fight - 1 :

                hps = stats[num_tour]["hps"]
                
                dfs = [0]*3
                for i in range(3):
                    fight_hps = hps[i+3]
                    dfs[i] = pd.DataFrame({"hps" : [fight_hps,hp_max[i+3]]} , index=None)
                    st.write(fight_hps)
                    st.bar_chart(dfs[i] , height=180)
            
            # Fight fini
            else:
                hps = stats[num_tour-1]["hps"]
                
                dfs = [0]*3
                for i in range(3):
                    fight_hps = hps[i+3]
                    dfs[i] = pd.DataFrame({"hps" : [fight_hps,hp_max[i+3]]} , index=None)
                    st.write(fight_hps)
                    st.bar_chart(dfs[i] , height=180)


        with cols[-1]:

            if num_tour < tour_engage:

                for r,red_champ in enumerate(self.results["red_team"]):
                    st.subheader(lvls[3+r])
                    try:
                        st.image("data/images/"+red_champ+".webp" , use_column_width=True)
                    except Exception:
                        st.image("data/images/"+red_champ+".jpg" , use_column_width=True)
                    

            else:
                distances = stats[num_tour]["positions"]
                for r,red_champ in enumerate(self.results["red_team"]):
                    st.subheader(lvls[3+r])

                    if distances[r+3] is None:
                        st.image("data/images/dead/"+red_champ+".jpg" , use_column_width=True)
                    else:
                        try:
                            st.image("data/images/"+red_champ+".webp" , use_column_width=True)
                        except Exception:
                            st.image("data/images/"+red_champ+".jpg" , use_column_width=True)


        
@st.cache_data
def get_data(path):

    with open(path , 'rb') as rf:
        results = pickle.load(rf)

    return Report(results)


def main():
    
    if "state_drake" not in st.session_state.keys():
        st.session_state.state_drake = -1
    if "state_baron" not in st.session_state.keys():
        st.session_state.state_baron = -1
    if "state_ancestral" not in st.session_state.keys():
        st.session_state.state_ancestral = -1
    if "match_selected" not in st.session_state.keys():
        st.session_state.match_selected = False

    if st.session_state.match_selected:

        tab1 , tab2 , tab3, tab4, tab5 = st.tabs(["Choix match" , "Résumé" , "Fight drake" , "Fight baron" , "Fight Ancestral"])

        with tab1:
            match_files = os.listdir("matchs")
            choix_match = st.selectbox(label="Choix du match" , options=match_files)
            report = get_data(path = "matchs/"+choix_match)

        with tab2:
            # report.page_resume()
            report.page_fights()


        with tab3:
            report.simulation_game(num_fight=0)

        with tab4:
            report.simulation_game(num_fight=1)

        with tab5:
            report.simulation_game(num_fight=2)

    else:
        match_files = os.listdir("matchs")
        choix_match = st.selectbox(label="Choix du match" , options=match_files)

        if st.button("Valider choix match" , key=2000):
            report = get_data(path = "matchs/"+choix_match)
            st.session_state.match_selected = True
            st.rerun()

    




if __name__ == "__main__":
    main()

