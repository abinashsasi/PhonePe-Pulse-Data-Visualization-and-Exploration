import io
import json
import pandas as pd
import mysql.connector
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_player import st_player
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_pandas_profiling import st_profile_report
from streamlit_extras.add_vertical_space import add_vertical_space

#------------get data from mysql database----------#
mysql_connection=mysql.connector.connect(
        host="localhost", #127.0.0.1
            user="root",
            password="",
            database='phonepe_pulse'
        )
cursor=mysql_connection.cursor()

cursor.execute("select * from agg_insur")
table1=cursor.fetchall()
s=cursor.column_names
Aggregated_Insurance=pd.DataFrame(table1,columns=cursor.column_names)

cursor.execute("select * from agg_trans")
table2=cursor.fetchall()
Aggregated_Transaction=pd.DataFrame(table2,columns=cursor.column_names)

cursor.execute("select * from agg_user")
table3=cursor.fetchall()
Aggregated_User=pd.DataFrame(table3,columns=cursor.column_names)

cursor.execute("select * from map_insur")
table4=cursor.fetchall()
Map_Insurance=pd.DataFrame(table4,columns=cursor.column_names)

cursor.execute("select * from map_trans")
table5=cursor.fetchall()
Map_Transaction=pd.DataFrame(table5,columns=cursor.column_names)

cursor.execute("select * from map_user")
table6=cursor.fetchall()
Map_User=pd.DataFrame(table6,columns=cursor.column_names)

cursor.execute("select * from top_insur_dist")
table7=cursor.fetchall()
Top_Insurance_Districtwise=pd.DataFrame(table7,columns=cursor.column_names)

cursor.execute("select * from top_insur_pin")
table8=cursor.fetchall()
Top_Insurance_Pincodewise=pd.DataFrame(table8,columns=cursor.column_names)

cursor.execute("select * from top_trans_dist")
table9=cursor.fetchall()
Top_Transaction_Districtwise=pd.DataFrame(table9,columns=cursor.column_names)

cursor.execute("select * from top_trans_pin")
table10=cursor.fetchall()
Top_Transaction_Pincodedwise=pd.DataFrame(table10,columns=cursor.column_names)

cursor.execute("select * from top_user_dist")
table11=cursor.fetchall()
Top_User_Districtwise=pd.DataFrame(table11,columns=cursor.column_names)

cursor.execute("select * from top_user_pin")
table12=cursor.fetchall()
Top_User_Pincodewise=pd.DataFrame(table12,columns=cursor.column_names)

mysql_connection.commit()
cursor.close()

if 'options' not in st.session_state:
    st.session_state['options']={'Aggregated_Insurance':'Aggregated_Insurance',
                          'Aggregated_Transaction':'Aggregated_Transaction',
                          'Aggregated_User':'Aggregated_User',
                          'Map_Insurance':'Map_Insurance',
                          'Map_Transaction':'Map_Transaction',
                          'Map_User':'Map_User',
                          'Top_Insurance_Districtwise':'Top_Insurance_Districtwise',
                          'Top_Insurance_Pincodewise':'Top_Insurance_Pincodewise',
                          'Top_Transaction_Districtwise':'Top_Transaction_Districtwise',
                          'Top_Transaction_Districtwise':'Top_Transaction_Districtwise',
                          'Top_User_Districtwise':'Top_User_Districtwise',
                          'Top_User_Pincodewise':'Top_User_Pincodewise'}

#df_list = [df for df in globals() if isinstance(globals()[df], pd.core.frame.DataFrame)]
    
#1
def trans_by_type(df,state,year,quarter):
    df=df[(df['State']==state) & (df['Year']==year)]
    
    if quarter == "ALL":
         df=df.groupby(['State','Year','Transaction_type'])[["Transaction_count","Transaction_amount"]].sum().reset_index()
    else:
         df=df[df['Quarter']==int(quarter)]
    col1,col2=st.columns(2)

    with col1:
         fig_amt= px.bar(df,x="Transaction_type",y='Transaction_amount')
         st.plotly_chart(fig_amt)
    with col2:
         fig_cnt=px.bar(df,x="Transaction_type",y='Transaction_count')
         st.plotly_chart(fig_cnt)
    
    




















#app
st.set_page_config(page_title="PHONEPE PULSE",
                    page_icon=None, 
                    layout="wide")

st.markdown(f""" 
<style>
    body {{
        background-color: {'#0000ff'};
    }}
    stChat {{
        background-color: {'#0000ff'};
    }}
    .stApp {{
        background: linear-gradient(to right, #ccccff, #ffccff);
        background-size: cover;
        transition: background 0.5s ease;
    }}
    h1,h2,h3,h4,h5,h6 {{
        color: #DC7633;
        font-family: 'Roboto', sans-serif;
    }}
    .stButton>button {{
        color: #0000ff;   
        background-color: ##DAF7A6;
        transition: all 0.3s ease-in-out;
    }}
    .stButton>button:hover {{
        color: #f3f3f3;
        background-color: #2b5876;
    }}
    .stTextInput>div>div>input {{
        color: #ffffff;
        background-color: #666699;
    }}
</style>
""",unsafe_allow_html=True)

with st.sidebar:
    option= option_menu(
    menu_title ="PhonePe Pulse",
    options = ["HOME","REPORTS","EXPLORE DATA","CONTACT"],
    icons =["bar-chart","house","toggles","at"],
    default_index=0,
    orientation="",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})
if option == "HOME":
    add_vertical_space(2)

    st.title(":violet[PHONEPE DATA VISUALIZATION AND EXPLORATION]")

    st_player(url = "https://youtu.be/Yy03rjSUIB8?si=nVq3AC5DO3U_mMte", height = 400)


    add_vertical_space(2)
    
    st.header("ABOUT PULSE")
    st.markdown(""":rainbow[The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data]""")
    st.markdown(''':rainbow[When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?]''')
    st.markdown(''':rainbow[This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.]''')
    st.markdown(''':rainbow[This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.]''')
    st.markdown(''':rainbow[PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.]''')

    st_player(url = "https://www.youtube.com/watch?v=c_1H6vivsiA", height = 400)

    add_vertical_space(2)

    col1,col2,col3=st.columns(3)

    total_reg_users = Top_User_Districtwise['Registered_users'].sum()
    col1.metric(
                label = 'TOTAL REGISTERED USERS',
                value = '{:.2f} Cr'.format(total_reg_users/100000000),
                delta = 'Forward Trend'
                )

    total_app_opens=Map_User["App_opens"].sum()
    col2.metric(
            label="TOTAL APP OPENS",
            value='{:.2f} cr'.format(total_app_opens/100000000),
            delta="Forward Trend"
    )

    col3.metric(
        label="Total Transaction Count",
        value='2000 cr +',
        delta="Forward Trend"
    )


    style_metric_cards(background_color='#5D3FD3')
    add_vertical_space(2)


    option=st.selectbox(label="SELECT DATASET",
                        options=st.session_state['options'].keys()
                        #key='df_list'
                        )

    tab1, tab2 = st.tabs(['Show Dataset', 'Download Dataset'])

    with tab1:
    
        sh_data=st.button("show")

    if sh_data:
            df_name=st.session_state['options'][option]
            df=globals()[df_name]
           
            st.dataframe(df_name)
           

    with tab2:
        col1,col2=st.columns(2)
        
        df_name=st.session_state['options'][option]
        df=globals()[df_name]

        csv = df.to_csv()
        json = df.to_json(orient ='records')
      

        col1.download_button(
                            "Download CSV file", data = csv,
                            file_name = f'{option}.csv',
                            mime = 'text/csv', key = 'csv'
                            )
        col2.download_button(
                            "Download JSON file", data = json,
                            file_name = f'{option}.json',
                            mime = 'application/json', key = 'json'
                            )
    
#..........................................
#............................................
        #..........................................


if option=="EXPLORE DATA":
   st.markdown(":violet[PHONEPE PULSE]")
   st.subheader("EXPLORE DATA")
   choice= option_menu(None,
    options = ["INSURANCE","TRANSACTION","USER","TOP CHARTS"],
    icons =["bar-chart","house","toggles","at"],
    default_index=0,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})
   

   if choice=="INSURANCE":
        
        state=Aggregated_Insurance["State"].unique()
        year=Aggregated_Insurance["Year"].unique()
        quarter=Aggregated_Insurance["Quarter"].unique()


        #1
        st.subheader(":blue[Insurance Transaction Amount and Count Breakdown]")
        col1,col2,col3=st.columns([5, 3, 1])
        
        #state1 = col1.selectbox("State", state, key='state1')
        year1 = col2.selectbox("Year", year, key='year1')
        q=["ALL"] + list(map(str, quarter))
        quarter1 = col3.selectbox("Quarter", q, key='quarter1')

        df_insur=Aggregated_Insurance[(Aggregated_Insurance['Year']==year1)]
        
        if quarter1 == "ALL":

            df_insur=df_insur.groupby('State')[["Transaction_count","Transaction_amount"]].sum().reset_index()
        else:
            df_insur=df_insur[df_insur['Quarter']==int(quarter1)]
        

       
        fig_inamt_bar= px.bar(df_insur,x="State",y='Transaction_amount',color="State", 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name="State")
        
        st.plotly_chart(fig_inamt_bar,use_container_width=True)
    
        '''fig_inamt_pie=px.pie(df_insur,values='Transaction_amount',names="",color="State", 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name="Transaction_type")
        
        col2.plotly_chart(fig_inamt_pie,use_container_width=True)'''
#---------------------------------------------------------------------------------------------
        #1.1
        fig_incnt_bar= px.bar(df_insur,x="Transaction_type",y='Transaction_count',color="Transaction_type", 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name="Transaction_type")
        
        st.plotly_chart(fig_incnt_bar,use_container_width=True)
    
        '''fig_incnt_pie=px.pie(df_insur,values='Transaction_count',names="Transaction_type",color="Transaction_type", 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name="Transaction_type")
        
        col2.plotly_chart(fig_incnt_pie,use_container_width=True)'''



















   
   if choice=="TRANSACTION":
       
        state=Aggregated_Transaction["State"].unique()
        year=Aggregated_Transaction["Year"].unique()
        quarter=Aggregated_Transaction["Quarter"].unique()


        #1
        st.subheader(":blue[Transaction Amount Count Breakdown by Type]")
        col1,col2,col3=st.columns([5, 3, 1])
        
        state1 = col1.selectbox("State", state, key='state1')
        year1 = col2.selectbox("Year", year, key='year1')
        q=["ALL"] + list(map(str, quarter))
        quarter1 = col3.selectbox("Quarter", q, key='quarter1')

        df1=Aggregated_Transaction[(Aggregated_Transaction['State']==state1) & (Aggregated_Transaction['Year']==year1)]
        
        if quarter1 == "ALL":

            df1=df1.groupby(['State','Transaction_type'])[["Transaction_count","Transaction_amount"]].sum().reset_index()
        else:
            df1=df1[df1['Quarter']==int(quarter1)]
        
        col1,col2=st.columns(2)

       
        fig_amt_bar= px.bar(df1,x="Transaction_type",y='Transaction_amount',color="Transaction_type", 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name="Transaction_type")
        
        col1.plotly_chart(fig_amt_bar,use_container_width=True)
    
        fig_amt_pie=px.pie(df1,values='Transaction_amount',names="Transaction_type",color="Transaction_type", 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name="Transaction_type")
        
        col2.plotly_chart(fig_amt_pie,use_container_width=True)
#---------------------------------------------------------------------------------------------
        #1.1
        fig_cnt_bar= px.bar(df1,x="Transaction_type",y='Transaction_count',color="Transaction_type", 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name="Transaction_type")
        
        col1.plotly_chart(fig_cnt_bar,use_container_width=True)
    
        fig_cnt_pie=px.pie(df1,values='Transaction_count',names="Transaction_type",color="Transaction_type", 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name="Transaction_type")
        
        col2.plotly_chart(fig_cnt_pie,use_container_width=True)

#------------------------------------------------------------------------------------------------------
        #2
        st.subheader(':blue[Transaction Hotspots - State]')

        col1, col2, buff = st.columns([1,1,4])

        year2 = col1.selectbox("Year", year, key='year2')
        q=["ALL"] + list(map(str, quarter))
        quarter2 = col2.selectbox("Quarter", q, key='quarter2')



        with open(r"C:/Users/abina/OneDrive/Desktop/phonepe/india_states.json") as f:
           data=json.load(f)

        df2=Map_Transaction[Map_Transaction["Year"]==year2]

        if quarter2 == "ALL":
            df2=df2.groupby("State")[['Transaction_Count','Transaction_Amount']].sum().reset_index()
        else:
            df2=df2[df2["Quarter"]==int(quarter2)]
            df2=df2.groupby("State")[['Transaction_Count','Transaction_Amount']].sum().reset_index()
        
        #col1,col2=st.columns(2)

        fig_amt_st=px.choropleth(df2, geojson= data, locations= "State", featureidkey= "properties.ST_NM",
                                    color= "State", color_continuous_scale= "Sunsetdark",
                                    hover_name= "State",title = f"{year2} TRANSACTION COUNT and TRANSACTION_AMOUNT",
                                    hover_data={'Transaction_Count':True,'Transaction_Amount':True})
        
        fig_amt_st.update_geos(fitbounds='locations', visible=False)

        
        fig_amt_st.update_layout(height=600, width=1300)  
        st.plotly_chart(fig_amt_st)
  #-----------------------------------------------------------------------------------------------      

        #3
        st.subheader(':blue[Transaction Hotspots - State]')

        col1, col2, buff = st.columns([1,1,4])

        year3 = col1.selectbox("Year", year, key='year3')
        q=["ALL"] + list(map(str, quarter))
        quarter3 = col2.selectbox("Quarter", q, key='quarter3')
    
        df3=Map_Transaction[Map_Transaction["Year"]==year3]
        if quarter3=="ALL":
            df3=df3.groupby(["District",'Latitude' ,'Longitude','State'])[['Transaction_Count','Transaction_Amount']].sum().reset_index()
        else:
            df3=df3[df3["Quarter"]==quarter3]
        
        # Create a scatter map
        fig_dist = px.scatter_mapbox(df3, lat = "Latitude", lon = "Longitude",
                        size = "Transaction_Amount", hover_name = "District",
                        hover_data = {"Transaction_Count": True, "Transaction_Amount": True, "Latitude":False, "Longitude":False},
                        color_discrete_sequence= px.colors.sequential.Plotly3
                        )

        fig_dist.update_layout(mapbox_style = 'carto-positron',  
                   mapbox_zoom = 3.45, mapbox_center = {"lat": 20.93684, "lon": 78.96288},
                   geo=dict(fitbounds="locations",
                               visible=False,  # Hide default map borders
                               lataxis=dict(range=[6.5, 35.9]),
                               lonaxis=dict(range=[68.1, 97.4]),
                               projection_type = 'equirectangular'), 
                   margin={"r":0,"t":0,"l":0,"b":0},height=600, width=1300)
        st.plotly_chart(fig_dist)


   if choice=="USER":
        
            state=Aggregated_User["State"].unique()
            year=Aggregated_User["Year"].unique()
            quarter=Aggregated_User["Quarter"].unique()


            #1
            st.subheader(":blue[Transaction Amount Count Breakdown by Type]")
            col1,col2,col3=st.columns([5, 3, 1])
            
            state1 = col1.selectbox("State", state, key='state1')
            year1 = col2.selectbox("Year", year, key='year1')
            q=["ALL"] + list(map(str, quarter))
            quarter1 = col3.selectbox("Quarter", q, key='quarter1')

            df1=Aggregated_User[(Aggregated_User['State']==state1) & (Aggregated_User['Year']==year1)]

            if quarter1 == "ALL":
                df1=df1.groupby("Brands")[['Transaction_Count','Percentage']].sum().reset_index()
            else:
                df1=df1[df1['Quarter']==int(quarter1)]

            fig1 = px.treemap(
                            df1,
                            path=['Brands'],
                            values='Transaction_Count',
                            color='Percentage',
                            color_continuous_scale='ylorbr',
                            #hover_data={'Transaction_Count':True,'Percentage': ':.2%'},
                            hover_name='Brands'
                            )

            fig1.update_layout(
                            width=975, height=600,
                            coloraxis_colorbar=dict(tickformat='.1%', len = 0.85),
                            margin=dict(l=20, r=20, t=0, b=20),
                            )

            fig1.update_traces(
                                hovertemplate = 
                                '<b>%{label}</b><br>Transaction Count: %{value}<br>Percentage: %{color:.2%}<extra></extra>'
                                )
            st.plotly_chart(fig1)

            #2

            with open(r"C:/Users/abina/OneDrive/Desktop/phonepe/india_states.json") as f:
                 data=json.load(f)
            st.subheader(':blue[User Hotspots - DISTRICT]')

            col1, col2, buff = st.columns([1,1,4])

            year2 = col1.selectbox("Year", year, key='year2')
            q=["ALL"] + list(map(str, quarter))
            quarter2 = col2.selectbox("Quarter", q, key='quarter2')
        
            df2=Map_User[Map_User["Year"]==year2]
            if quarter2=="ALL":
                df2=df2.groupby(["District",'Latitude' ,'Longitude','State'])[['Registered_user','App_opens']].sum().reset_index()
            else:
                df2=df2[df2["Quarter"]==int(quarter2)]
            
            # Create a scatter map
            fig_dist2 = px.scatter_mapbox(df2, lat = "Latitude", lon = "Longitude",
                            size = "Registered_user", hover_name = "District",
                            hover_data = {"Latitude":False, "Longitude":False,'App_opens':True},
                            color_discrete_sequence= px.colors.sequential.Plotly3
                            )

            fig_dist2.update_layout(mapbox_style = 'carto-positron',  
                    mapbox_zoom = 3.45, mapbox_center = {"lat": 20.93684, "lon": 78.96288},
                    geo=dict(fitbounds="locations",
                                visible=False,  # Hide default map borders
                                lataxis=dict(range=[6.5, 35.9]),
                                lonaxis=dict(range=[68.1, 97.4]),
                                projection_type = 'equirectangular'), 
                    margin={"r":0,"t":0,"l":0,"b":0},height=600, width=1300)
            st.plotly_chart(fig_dist2)

            #3
            st.subheader(':blue[Number of app opens by District]')

            col1, col2, buff = st.columns([1,1,4])

            year3 = col1.selectbox("Year", year, key='year3')
            q=["ALL"] + list(map(str, quarter))
            quarter3 = col2.selectbox("Quarter", q, key='quarter3')
        
            df3=Map_User[Map_User["Year"]==year2]
            if quarter3=="ALL":
                df3=df3.groupby(["District",'Latitude' ,'Longitude','State'])['App_opens'].sum().reset_index()
            else:
                df3=df3[df3["Quarter"]==int(quarter2)]

            fig4 = px.density_mapbox(df3,
                        lat='Latitude', lon='Longitude',
                        z='App_opens', radius=20,
                        center=dict(lat=20.5937,lon=78.9629),
                        zoom=3, hover_name='District',
                        mapbox_style="stamen-watercolor",
                        opacity=0.8,hover_data={'Latitude': False,'Longitude': False,'State': True
                                    },
                    color_continuous_scale = 'Blues'
                    )

            fig4.update_layout(
                            margin=dict(l=20, r=20, t=60, b=20),
                            mapbox=dict(layers=[
                                                dict(
                                                        sourcetype='geojson',
                                                        source=data,
                                                        type='line',
                                                        color='white',
                                                        opacity=0.8,
                                                        )
                                                    ]
                                        ),
                            width=925, height=600,
                            coloraxis_colorbar=dict(len=0.9),
                            title={
                                    'text': 'App Opens Density Map',
                                    'x': 0.43,
                                    'xanchor': 'center',
                                    'y': 0.09,
                                    'yanchor': 'bottom',
                                    'font': dict(color='black')
                                    }
                            )

            st.plotly_chart(fig4)

            

            