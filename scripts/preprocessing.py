import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler 
from sklearn.feature_selection import SelectKBest

#Importation de données
path = "D:/MasterFDIA/Docmemoire/Row/"
rco = pd.read_excel(path + 'data_V0.xlsx')

#rco = rco[rco.columns[rco.isna().sum()/rco.shape[0]<0.90]]
rco.YEAR[rco.YEAR=='ceftria"']=2021 # Remplacer ceftria par 2021
#rco.drop(rco.loc[rco['YEAR']==2021].index, inplace=True) #suppression des données de 2021
rco.drop(['N','M','T','PROFESSION','CHIM','CHIR','YEAR','ETHN'],1,inplace=True)
rco.drop(rco.loc[rco['COMP']==20200313.0].index, inplace=True) # 
rco.drop(rco.loc[rco['COMP']==5.0].index, inplace=True) # 
rco.drop(rco.loc[rco['COMP']==2.0].index, inplace=True) # 
rco.drop(['COMP'],1,inplace=True)
rco.drop(rco.loc[rco['SEXE']=='lx'].index, inplace=True)

rco["CAS"] = rco["MORP"]
rco.CAS[rco.CAS==9687.0]='LB' 
rco.CAS[rco.CAS==9590.0]='LB'
rco.CAS[rco.CAS==9591.0]='LB'
rco.CAS[rco.CAS==9596.0]='LB'
rco.CAS[rco.CAS==9597.0]='LB'
rco.CAS[rco.CAS==9650.0]='LB'
rco.CAS[rco.CAS==9651.0]='LB'
rco.CAS[rco.CAS==9652.0]='LB'
rco.CAS[rco.CAS==9653.0]='LB'
rco.CAS[rco.CAS==9654.0]='LB'
rco.CAS[rco.CAS==9655.0]='LB'
rco.CAS[rco.CAS==9659.0]='LB'
rco.CAS[rco.CAS==9663.0]='LB'
rco.CAS[rco.CAS==9664.0]='LB'
rco.CAS[rco.CAS==9665.0]='LB'
rco.CAS[rco.CAS==9667.0]='LB'
rco.CAS[rco.CAS==9670.0]='LB'
rco.CAS[rco.CAS==9671.0]='LB'
rco.CAS[rco.CAS==9673.0]='LB'
rco.CAS[rco.CAS==9675.0]='LB'
rco.CAS[rco.CAS==9678.0]='LB'
rco.CAS[rco.CAS==9679.0]='LB'
rco.CAS[rco.CAS==9680.0]='LB'
rco.CAS[rco.CAS==9684.0]='LB'
rco.CAS[rco.CAS==9687.0]='LB'
rco.CAS[rco.CAS==9688.0]='LB'
rco.CAS[rco.CAS==9689.0]='LB'
rco.CAS[rco.CAS==9690.0]='LB'
rco.CAS[rco.CAS==9691.0]='LB'
rco.CAS[rco.CAS==9695.0]='LB'
rco.CAS[rco.CAS==9698.0]='LB'
rco.CAS[rco.CAS==9699.0]='LB'
rco.CAS[rco.CAS==9702.0]='LB'
rco.CAS[rco.CAS==9705.0]='LB'
rco.CAS[rco.CAS==9708.0]='LB'
rco.CAS[rco.CAS==9709.0]='LB'
rco.CAS[rco.CAS==9712.0]='LB'
rco.CAS[rco.CAS==9714.0]='LB'
rco.CAS[rco.CAS==9716.0]='LB'
rco.CAS[rco.CAS==9717.0]='LB'
rco.CAS[rco.CAS==9719.0]='LB'
rco.CAS[rco.CAS==9725.0]='LB'
rco.CAS[rco.CAS==9726.0]='LB'
rco.CAS[rco.CAS==9728.0]='LB'
rco.CAS[rco.CAS==9729.0]='LB'
rco.CAS[rco.CAS==9735.0]='LB'
rco.CAS[rco.CAS==9737.0]='LB'
rco.CAS[rco.CAS==9738.0]='LB'
rco.CAS[rco.CAS==9811.0]='LB'
rco.CAS[rco.CAS==9812.0]='LB'
rco.CAS[rco.CAS==9813.0]='LB'
rco.CAS[rco.CAS==9814.0]='LB'
rco.CAS[rco.CAS==9815.0]='LB'
rco.CAS[rco.CAS==9816.0]='LB'
rco.CAS[rco.CAS==9817.0]='LB'
rco.CAS[rco.CAS==9818.0]='LB'
rco.CAS[rco.CAS==9823.0]='LB'
rco.CAS[rco.CAS==9827.0]='LB'
rco.CAS[rco.CAS!='LB']='AC'
rco.drop(['MORP'],1,inplace=True)

rco["AttH"] = "Non"
rco.AttH[rco.TOPO==220]='Oui'

rco["AttD"] = "Non"
rco.AttD[rco.TOPO==268]='Oui'
rco.AttD[rco.TOPO==269]='Oui'

rco["AttR"] = "Non"
rco.AttR[rco.TOPO==8316]='Oui'
rco.AttR[rco.TOPO==8317]='Oui'
rco.AttR[rco.TOPO==8318]='Oui'
rco.AttR[rco.TOPO==8319]='Oui'

rco["Dysp"] = "Non"
rco.Dysp[rco.TOPO==390]='Oui'
rco.Dysp[rco.TOPO==398]='Oui'
rco.Dysp[rco.TOPO==399]='Oui'

rco["AttMed"] = "Non"
rco.AttMed[rco.TOPO==710]='Oui'
rco.AttMed[rco.TOPO==711]='Oui'
rco.AttMed[rco.TOPO==712]='Oui'
rco.AttMed[rco.TOPO==713]='Oui'
rco.AttMed[rco.TOPO==714]='Oui'
rco.AttMed[rco.TOPO==715]='Oui'
rco.AttMed[rco.TOPO==716]='Oui'
rco.AttMed[rco.TOPO==717]='Oui'
rco.AttMed[rco.TOPO==718]='Oui'
rco.AttMed[rco.TOPO==719]='Oui'
rco.AttMed[rco.TOPO==720]='Oui'
rco.AttMed[rco.TOPO==721]='Oui'
rco.AttMed[rco.TOPO==722]='Oui'
rco.AttMed[rco.TOPO==723]='Oui'
rco.AttMed[rco.TOPO==724]='Oui'
rco.AttMed[rco.TOPO==725]='Oui'
rco.AttMed[rco.TOPO==728]='Oui'
rco.AttMed[rco.TOPO==729]='Oui'
rco.AttMed[rco.TOPO==739]='Oui'
rco.AttMed[rco.TOPO==740]='Oui'
rco.AttMed[rco.TOPO==741]='Oui'
rco.AttMed[rco.TOPO==749]='Oui'
rco.AttMed[rco.TOPO==750]='Oui'
rco.AttMed[rco.TOPO==751]='Oui'
rco.AttMed[rco.TOPO==752]='Oui'
rco.AttMed[rco.TOPO==753]='Oui'
rco.AttMed[rco.TOPO==754]='Oui'
rco.AttMed[rco.TOPO==755]='Oui'

rco["AttMen"] = "Non"
rco.AttMen[rco.TOPO==700]='Oui'
rco.AttMen[rco.TOPO==701]='Oui'
rco.AttMen[rco.TOPO==709]='Oui'

rco["AttOvaire"] = "Non"
rco.AttOvaire[rco.TOPO==56]='Oui'

rco["MassAbdo"] = "Non"
rco.MassAbdo[rco.TOPO==150]='Oui'
rco.MassAbdo[rco.TOPO==151]='Oui'
rco.MassAbdo[rco.TOPO==152]='Oui'
rco.MassAbdo[rco.TOPO==153]='Oui'
rco.MassAbdo[rco.TOPO==154]='Oui'
rco.MassAbdo[rco.TOPO==155]='Oui'
rco.MassAbdo[rco.TOPO==156]='Oui'
rco.MassAbdo[rco.TOPO==157]='Oui'
rco.MassAbdo[rco.TOPO==158]='Oui'
rco.MassAbdo[rco.TOPO==159]='Oui'
rco.MassAbdo[rco.TOPO==160]='Oui'
rco.MassAbdo[rco.TOPO==161]='Oui'
rco.MassAbdo[rco.TOPO==162]='Oui'
rco.MassAbdo[rco.TOPO==163]='Oui'
rco.MassAbdo[rco.TOPO==164]='Oui'
rco.MassAbdo[rco.TOPO==165]='Oui'
rco.MassAbdo[rco.TOPO==166]='Oui'
rco.MassAbdo[rco.TOPO==168]='Oui'
rco.MassAbdo[rco.TOPO==169]='Oui'
rco.MassAbdo[rco.TOPO==170]='Oui'
rco.MassAbdo[rco.TOPO==171]='Oui'
rco.MassAbdo[rco.TOPO==172]='Oui'
rco.MassAbdo[rco.TOPO==173]='Oui'
rco.MassAbdo[rco.TOPO==178]='Oui'
rco.MassAbdo[rco.TOPO==179]='Oui'
rco.MassAbdo[rco.TOPO==180]='Oui'
rco.MassAbdo[rco.TOPO==181]='Oui'
rco.MassAbdo[rco.TOPO==182]='Oui'
rco.MassAbdo[rco.TOPO==183]='Oui'
rco.MassAbdo[rco.TOPO==184]='Oui'
rco.MassAbdo[rco.TOPO==185]='Oui'
rco.MassAbdo[rco.TOPO==186]='Oui'
rco.MassAbdo[rco.TOPO==187]='Oui'
rco.MassAbdo[rco.TOPO==189]='Oui'
rco.MassAbdo[rco.TOPO==199]='Oui'

rco["Gangl"] = "Non"
rco.Gangl[rco.TOPO==770]='Oui'
rco.Gangl[rco.TOPO==771]='Oui'
rco.Gangl[rco.TOPO==772]='Oui'
rco.Gangl[rco.TOPO==773]='Oui'
rco.Gangl[rco.TOPO==774]='Oui'
rco.Gangl[rco.TOPO==775]='Oui'
rco.Gangl[rco.TOPO==776]='Oui'
rco.Gangl[rco.TOPO==777]='Oui'
rco.Gangl[rco.TOPO==778]='Oui'

rco["Stad"] = np.nan
rco.Stad[rco.STADE=="1x"]='Stade I'
rco.Stad[rco.STADE=="1A"]='Stade I'
rco.Stad[rco.STADE=="1B"]='Stade I'
rco.Stad[rco.STADE=="2x"]='Stade II'
rco.Stad[rco.STADE=="2A"]='Stade II'
rco.Stad[rco.STADE=="2B"]='Stade II'
rco.Stad[rco.STADE=="2b"]='Stade II'
rco.Stad[rco.STADE=="2C"]='Stade II'
rco.Stad[rco.STADE=="2c"]='Stade II'
rco.Stad[rco.STADE=="3x"]='Stade III'
rco.Stad[rco.STADE=="3A"]='Stade III'
rco.Stad[rco.STADE=="3a"]='Stade III'
rco.Stad[rco.STADE=="3B"]='Stade III'
rco.Stad[rco.STADE=="3C"]='Stade III'
rco.Stad[rco.STADE=="4x"]='Stade IV'
rco.Stad[rco.STADE=="4A"]='Stade IV'
rco.Stad[rco.STADE=="4B"]='Stade IV'
rco.Stad[rco.STADE=="C+"]='Stade IV'
rco.Stad[rco.STADE=="C-"]='Stade IV'
rco.Stad[rco.STADE=="LR"]='Stade IV'
rco.Stad[rco.STADE=="Ax"]='Stade IV'
rco.Stad[rco.STADE=="LX"]='Stade IV'
rco.Stad[rco.STADE=="Lx"]='Stade IV'
rco.Stad[rco.STADE=="Mx"]='Stade IV'
rco.Stad[rco.STADE=="Rx"]='Stade IV'
rco.Stad[rco.STADE=="MS"]='Stade IV'
rco.Stad[rco.STADE=="Ax"]='Stade IV'
rco.Stad[rco.STADE=="XX"]='Stade IV'
rco.Stad[rco.STADE=="Xx"]='Stade IV'
rco.Stad[rco.STADE=="c-"]='Stade IV'
rco.Stad[rco.STADE=="1r"]='Stade IV'
rco.Stad[rco.STADE=="1x"]='Stade IV'
rco.Stad[rco.STADE=="xx"]='Stade IV'
rco.Stad[rco['Stad'].isna()]='Stade IV'

rco.drop(['STADE','TOPO','CASES','CAUS','CIM1','MULT'],1,inplace=True)

def imputation(rco):
    #rco.fillna(-999, inplace=True)
    #return rco.dropna(axis=0)
    #rco['is na'] = rco['STADE'].isna()
    rco = rco.fillna(-999)
    return rco

missing_rate = rco.isna().sum()/rco.shape[0]
rco.columns[(missing_rate < 0.9) & (missing_rate > 0.80)]

def encodage(rco):
    code = {'AC':0,'LB':1,'Garçon':1,'Fille':2,'Oui':1,'Non':0,'Stade I':1,'Stade II':2,'Stade III':3,
            'Stade IV':4,'6c':0,'10b':2,'6a':3,'12b':4,'2e':6,'1a':7,'9b':8,'7a':9,'8e':10,'7c':11,
            '1e':12,'3e':13,'1b':14,'3f':15,'3c':16,'2b':17,'1c':18,'9a':19,'3b':20,'11f':21,'10c':22,
            '4a':23,'2a':24,'9d':25,'3d':26,'7b':27,'8a':28,'10e':29,'11e':30,'2c':31}
    for col in rco.select_dtypes('object').columns:
        rco.loc[:,col]=rco[col].map(code)
    return rco

def preprocessing(rco):

    rco = encodage(rco)
    rco = imputation(rco)
    
    x = rco.drop('CAS', axis=1)
    y = rco['CAS']
    
    print(y.value_counts())
    return x, y

rco.to_excel("D:/MasterFDIA/Docmemoire/prediLB/assets/original_dataset/dt_rco.xlsx", index = False)
rco.to_csv("D:/MasterFDIA/Docmemoire/prediLB/assets/original_dataset/dt_rco.csv", index = False)