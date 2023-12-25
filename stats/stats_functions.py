# Import
import utils
import pandas as pd
import geopandas as gpd



def map_plot_data():

    # Get crime data
    df_crimes = utils.read_and_load_crimes_committed()

    # Clean Data
    df_crimes = clean_data_map_plot(df_crimes)

    # Get number of crimes per regions/department per year
    # df_crimes_dep ,df_crimes_regions = number_crimes_per_location(df_crimes)
    df_crimes_dep ,df_crimes_regions = tauxpourmille_crimes_per_location(df_crimes)

    # Get geoJson data
    df_gj_dep, df_gj_regions = load_geoJson_data()

    # Get merged geoJson/crime_data Df
    df_dep, df_regions = merge_crime_and_geoj_dfs(df_crimes_dep, df_crimes_regions,df_gj_dep,df_gj_regions)

    # Make Dfs pretty
    df_dep, df_regions = make_df_pretty(df_dep, df_regions)

    return df_dep, df_regions



def clean_data_map_plot(df_crimes):

    df_crimes['faits'] = df_crimes['faits'].astype(int) # set crimes values as inegers
    df_crimes = df_crimes.rename(columns={'faits':'nº crimes','annee':'year'}) # Rename colomns
    df_crimes['tauxpourmille'] = df_crimes['tauxpourmille'].apply(lambda x: x.replace(',','.')).astype(float) # set crimes values as floats
    df_crimes = df_crimes.rename(columns={'tauxpourmille':'crimes/1k hab','annee':'year'}) # Rename colomns

    return df_crimes



def tauxpourmille_crimes_per_location(df_crimes):

    # Get number of crimes per  regions/department
    df_crimes_regions =  df_crimes.groupby(['Code.région','year']).sum()[['crimes/1k hab']].reset_index()
    df_crimes_dep =  df_crimes.groupby(['Code.département','year']).sum()[['crimes/1k hab']].reset_index()

    return df_crimes_dep ,df_crimes_regions



def number_crimes_per_location(df_crimes):

    # Get number of crimes per  regions/department
    df_crimes_dep = df_crimes.groupby(['Code.département','year']).sum().reset_index()
    df_crimes_regions = df_crimes.groupby(['Code.région','year']).sum().reset_index()

    return df_crimes_dep ,df_crimes_regions



def load_geoJson_data(simplicity=4500):

    # Load geoJson data
    df_gj_dep = gpd.read_file('./data/geoJson_data/dep_geojson.geojson')
    df_gj_regions = gpd.read_file('./data/geoJson_data/regions_geojson.geojson')

    # Siplify data
    df_gj_dep["geometry"] = (df_gj_dep.to_crs(df_gj_dep.estimate_utm_crs()).simplify(simplicity).to_crs(df_gj_dep.crs))
    df_gj_regions["geometry"] = (df_gj_regions.to_crs(df_gj_regions.estimate_utm_crs()).simplify(simplicity).to_crs(df_gj_regions.crs))

    return df_gj_dep, df_gj_regions



def merge_crime_and_geoj_dfs(df_crimes_dep, df_crimes_regions,df_gj_dep,df_gj_regions):

    # Rename columns
    df_crimes_dep = df_crimes_dep.rename(columns={'Code.département':'code'})
    df_crimes_regions = df_crimes_regions.rename(columns={'Code.région':'code'})

    # Merge geoJson data with crime data
    df_dep = pd.merge(df_gj_dep, df_crimes_dep, on='code', how='outer').dropna() # Merge department Dfs
    df_regions = pd.merge(df_gj_regions, df_crimes_regions, on='code', how='outer').dropna() # Merge regions Dfs

    return df_dep, df_regions



def make_df_pretty(df_dep, df_regions):
    # Make df "pretty"
    df_dep = df_dep.rename(columns={'nom':'location'}) # Rename colomns
    df_regions = df_regions.rename(columns={'nom':'location'}) # Rename colomns
    df_dep['year'] = df_dep['year'].apply(lambda x: '20'+x)
    df_regions['year'] = df_regions['year'].apply(lambda x: '20'+x)
    df_dep = df_dep.set_index('location') # set depart name as index
    df_regions = df_regions.set_index('location') # set region name as index

    return df_dep, df_regions



def map_plot_data_gend():

    # Load gendarmerie data
    df = pd.read_csv('./data/gend_and_services.csv')

    # Group by location
    df_nb_gend_dep = df.groupby(['Department']).sum()[['Number of Gendarmerie']].reset_index()
    df_nb_gend_regions = df.groupby(['Region']).sum()[['Number of Gendarmerie']].reset_index()

    # Load geoJson data
    df_gj_dep = gpd.read_file('./data/geoJson_data/dep_geojson.geojson')
    df_gj_regions = gpd.read_file('./data/geoJson_data/regions_geojson.geojson')

    # Siplify data
    df_gj_dep["geometry"] = (df_gj_dep.to_crs(df_gj_dep.estimate_utm_crs()).simplify(4500).to_crs(df_gj_dep.crs))
    df_gj_regions["geometry"] = (df_gj_regions.to_crs(df_gj_regions.estimate_utm_crs()).simplify(4500).to_crs(df_gj_regions.crs))

    # Rename columns
    df_nb_gend_dep = df_nb_gend_dep.rename(columns={'Department':'code'})
    df_nb_gend_regions = df_nb_gend_regions.rename(columns={'Region':'nom'})

    # Clean data
    for i in range(len(df_nb_gend_dep)):
        if df_nb_gend_dep.iloc[i]['code'] in ['1','2','3','4','5','6','7','8','9']:
            df_nb_gend_dep.at[i,'code'] =  '0' + df_nb_gend_dep.at[i,'code']

    # Merge geoJson data with crime data
    df_dep = pd.merge(df_gj_dep, df_nb_gend_dep, on='code', how='outer').dropna() # Merge department Dfs
    df_regions = pd.merge(df_gj_regions, df_nb_gend_regions, on='nom', how='outer').dropna() # Merge regions Dfs

    # Make df "pretty"
    df_dep = df_dep.rename(columns={'nom':'location'}) # Rename colomns
    df_regions = df_regions.rename(columns={'nom':'location'}) # Rename colomns
    df_dep = df_dep.set_index('location') # set depart name as index
    df_regions = df_regions.set_index('location') # set region name as index

    return df_dep, df_regions



def map_plot_data_nubtotal():

    # Get crime data
    df_crimes = utils.read_and_load_crimes_committed()

    # Clean Data
    df_crimes = clean_data_map_plot(df_crimes)

    # Get number of crimes per regions/department per year
    df_crimes_dep ,df_crimes_regions = number_crimes_per_location(df_crimes)

    # Get geoJson data
    df_gj_dep, df_gj_regions = load_geoJson_data()

    # Get merged geoJson/crime_data Df
    df_dep, df_regions = merge_crime_and_geoj_dfs(df_crimes_dep, df_crimes_regions,df_gj_dep,df_gj_regions)

    # Make Dfs pretty
    df_dep, df_regions = make_df_pretty(df_dep, df_regions)

    return df_dep, df_regions