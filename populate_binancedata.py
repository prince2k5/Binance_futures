from binance.client import Client
import pandas as pd
import streamlit as st

# API_KEY=st.secrets["API"]["KEY"]
# API_SECRET=st.secrets["API"]["SECRET"]
# API_KEY=open(r"C:\Users\princ\Documents\public_key.txt",'r').read()
# API_SECRET=open(r"C:\Users\princ\Documents\private_key.txt",'r').read()



df = pd.DataFrame(columns=['Symbol', 'Funding Rate', 'Leverage 1', 'Notional Cap 1', 'Leverage 2', 'Notional Cap 2', 'Leverage 3', 'Notional Cap 3', 'Leverage 4', 'Notional Cap 4', 'Leverage 5', 'Notional Cap 5', 'Leverage 6', 'Notional Cap 6', 'Leverage 7', 'Notional Cap 7', 'Leverage 8', 'Notional Cap 8', 'Leverage 9', 'Notional Cap 9', 'Leverage 10', 'Notional Cap 10'])

interested_symbols = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'AKROUSDT', 'BCHUSDT', 'BTSUSDT', 'DODOUSDT', 'DOTUSDT', 'EOSUSDT', 'ETCUSDT', 'LENDUSDT', 'LINKUSDT', 'SCUSDT', 'TRXUSDT', 'XRPUSDT', 'YFIIUSDT', '1000BTTCUSDT', '1INCHUSDT', 'ANCUSDT', 'APEUSDT', 'AVAXUSDT', 'AXSUSDT', 'BALUSDT', 'BTCSTUSDT', 'BTTUSDT', 'BZRXUSDT', 'CELRUSDT', 'CHZUSDT', 'COMPUSDT', 'DASHUSDT', 'DENTUSDT', 'DOGEUSDT', 'EGLDUSDT', 'FILUSDT', 'FTMUSDT', 'GMTUSDT', 'GRTUSDT', 'HBARUSDT', 'HOTUSDT', 'IOTAUSDT', 'KEEPUSDT', 'KNCUSDT', 'KSMUSDT', 'LTCUSDT', 'MANAUSDT', 'MATICUSDT', 'MKRUSDT', 'NEARUSDT', 'NEOUSDT', 'NUUSDT', 'ONTUSDT', 'QTUMUSDT', 'RAYUSDT', 'RUNEUSDT', 'SANDUSDT', 'STORJUSDT', 'SXPUSDT', 'THETAUSDT', 'TLMUSDT', 'XLMUSDT', 'XMRUSDT', 'YFIUSDT', 'ZECUSDT', 'ZENUSDT', 'ZRXUSDT', 'ALPHAUSDT', 'APTUSDT', 'CHRUSDT', 'COTIUSDT', 'CRVUSDT', 'OCEANUSDT', '1000LUNCUSDT', '1000XECUSDT', 'AAVEUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ANKRUSDT', 'ANTUSDT', 'API3USDT', 'ARPAUSDT', 'ARUSDT', 'ATAUSDT', 'ATOMUSDT', 'AUDIOUSDT', 'BAKEUSDT', 'BANDUSDT', 'BATUSDT', 'BELUSDT', 'BLUEBIRDUSDT', 'BLZUSDT', 'BTCDOMUSDT', 'C98USDT', 'CELOUSDT', 'CTKUSDT', 'CTSIUSDT', 'CVXUSDT', 'DEFIUSDT', 'DOTECOUSDT', 'DUSKUSDT', 'DYDXUSDT', 'ENJUSDT', 'ENSUSDT', 'FLMUSDT', 'FLOWUSDT', 'FOOTBALLUSDT', 'GALAUSDT', 'GALUSDT', 'GTCUSDT', 'ICPUSDT', 'ICXUSDT', 'IMXUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTXUSDT', 'JASMYUSDT', 'KAVAUSDT', 'KLAYUSDT', 'LDOUSDT', 'LINAUSDT', 'LITUSDT', 'LPTUSDT', 'LRCUSDT', 'LUNA2USDT', 'MASKUSDT', 'MTLUSDT', 'NKNUSDT', 'OGNUSDT', 'OMGUSDT', 'ONEUSDT', 'OPUSDT', 'PEOPLEUSDT', 'QNTUSDT', 'REEFUSDT', 'RENUSDT', 'RLCUSDT', 'ROSEUSDT', 'RSRUSDT', 'RVNUSDT', 'SKLUSDT', 'SNXUSDT', 'SPELLUSDT', 'STGUSDT', 'STMXUSDT', 'SUSHIUSDT', 'TOMOUSDT', 'UNFIUSDT', 'UNIUSDT', 'VETUSDT', 'WOOUSDT', 'XEMUSDT', 'XTZUSDT', 'ZILUSDT', 'SOLUSDT', 'HNTUSDT', 'CVCUSDT', 'DARUSDT', 'WAVESUSDT', 'BNXUSDT', 'FTTUSDT', 'LUNAUSDT', 'SFPUSDT', 'SRMUSDT']

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


@st.cache
def get_data():
    df = pd.DataFrame()
    for symbol in interested_symbols:
        new_row = []
        try:
            brackets = client.futures_leverage_bracket(symbol=symbol)[0]
            funding_rate = client.futures_funding_rate(symbol=symbol)[-1]['fundingRate']
        except Exception as e:
            continue

        for i in range(len(brackets['brackets'])):
            symbol = brackets['symbol']
            new_row.append(brackets['brackets'][i]['initialLeverage'])
            new_row.append(brackets['brackets'][i]['notionalCap'])

            if len(new_row) == 20:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': [new_row[4]],
                    'Notional Cap 3': [new_row[5]],
                    'Leverage 4': [new_row[6]],
                    'Notional Cap 4': [new_row[7]],
                    'Leverage 5': [new_row[8]],
                    'Notional Cap 5': [new_row[9]],
                    'Leverage 6': [new_row[10]],
                    'Notional Cap 6': [new_row[11]],
                    'Leverage 7': [new_row[12]],
                    'Notional Cap 7': [new_row[13]],
                    'Leverage 8': [new_row[14]],
                    'Notional Cap 8': [new_row[15]],
                    'Leverage 9': [new_row[16]],
                    'Notional Cap 9': [new_row[17]],
                    'Leverage 10': [new_row[18]],
                    'Notional Cap 10': [new_row[19]],
                })
            elif len(new_row) == 18:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': [new_row[4]],
                    'Notional Cap 3': [new_row[5]],
                    'Leverage 4': [new_row[6]],
                    'Notional Cap 4': [new_row[7]],
                    'Leverage 5': [new_row[8]],
                    'Notional Cap 5': [new_row[9]],
                    'Leverage 6': [new_row[10]],
                    'Notional Cap 6': [new_row[11]],
                    'Leverage 7': [new_row[12]],
                    'Notional Cap 7': [new_row[13]],
                    'Leverage 8': [new_row[14]],
                    'Notional Cap 8': [new_row[15]],
                    'Leverage 9': [new_row[16]],
                    'Notional Cap 9': [new_row[17]],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
            elif len(new_row) == 16:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': [new_row[4]],
                    'Notional Cap 3': [new_row[5]],
                    'Leverage 4': [new_row[6]],
                    'Notional Cap 4': [new_row[7]],
                    'Leverage 5': [new_row[8]],
                    'Notional Cap 5': [new_row[9]],
                    'Leverage 6': [new_row[10]],
                    'Notional Cap 6': [new_row[11]],
                    'Leverage 7': [new_row[12]],
                    'Notional Cap 7': [new_row[13]],
                    'Leverage 8': [new_row[14]],
                    'Notional Cap 8': [new_row[15]],
                    'Leverage 9': ["Nan"],
                    'Notional Cap 9': ["NaN"],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
            elif len(new_row) == 14:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': [new_row[4]],
                    'Notional Cap 3': [new_row[5]],
                    'Leverage 4': [new_row[6]],
                    'Notional Cap 4': [new_row[7]],
                    'Leverage 5': [new_row[8]],
                    'Notional Cap 5': [new_row[9]],
                    'Leverage 6': [new_row[10]],
                    'Notional Cap 6': [new_row[11]],
                    'Leverage 7': [new_row[12]],
                    'Notional Cap 7': [new_row[13]],
                    'Leverage 8': ["NaN"],
                    'Notional Cap 8': ["NaN"],
                    'Leverage 9': ['NaN'],
                    'Notional Cap 9': ["NaN"],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
            elif len(new_row) == 12:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': [new_row[4]],
                    'Notional Cap 3': [new_row[5]],
                    'Leverage 4': [new_row[6]],
                    'Notional Cap 4': [new_row[7]],
                    'Leverage 5': [new_row[8]],
                    'Notional Cap 5': [new_row[9]],
                    'Leverage 6': [new_row[10]],
                    'Notional Cap 6': [new_row[11]],
                    'Leverage 7': ["NaN"],
                    'Notional Cap 7': ["NaN"],
                    'Leverage 8': ["NaN"],
                    'Notional Cap 8': ["NaN"],
                    'Leverage 9': ['NaN'],
                    'Notional Cap 9': ["NaN"],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
            elif len(new_row) == 10:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': [new_row[4]],
                    'Notional Cap 3': [new_row[5]],
                    'Leverage 4': [new_row[6]],
                    'Notional Cap 4': [new_row[7]],
                    'Leverage 5': [new_row[8]],
                    'Notional Cap 5': [new_row[9]],
                    'Leverage 6': ["NaN"],
                    'Notional Cap 6': ["NaN"],
                    'Leverage 7': ["NaN"],
                    'Notional Cap 7': ["NaN"],
                    'Leverage 8': ["NaN"],
                    'Notional Cap 8': ["NaN"],
                    'Leverage 9': ['NaN'],
                    'Notional Cap 9': ["NaN"],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
            elif len(new_row) == 8:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': [new_row[4]],
                    'Notional Cap 3': [new_row[5]],
                    'Leverage 4': [new_row[6]],
                    'Notional Cap 4': [new_row[7]],
                    'Leverage 5': ["NaN"],
                    'Notional Cap 5': ["NaN"],
                    'Leverage 6': ["NaN"],
                    'Notional Cap 6': ["NaN"],
                    'Leverage 7': ["NaN"],
                    'Notional Cap 7': ["NaN"],
                    'Leverage 8': ["NaN"],
                    'Notional Cap 8': ["NaN"],
                    'Leverage 9': ['NaN'],
                    'Notional Cap 9': ["NaN"],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
            elif len(new_row) == 6:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': [new_row[4]],
                    'Notional Cap 3': [new_row[5]],
                    'Leverage 4': ["NaN"],
                    'Notional Cap 4': ["NaN"],
                    'Leverage 5': ["NaN"],
                    'Notional Cap 5': ["NaN"],
                    'Leverage 6': ["NaN"],
                    'Notional Cap 6': ["NaN"],
                    'Leverage 7': ["NaN"],
                    'Notional Cap 7': ["NaN"],
                    'Leverage 8': ["NaN"],
                    'Notional Cap 8': ["NaN"],
                    'Leverage 9': ['NaN'],
                    'Notional Cap 9': ["NaN"],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
            elif len(new_row) == 4:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': [new_row[2]],
                    'Notional Cap 2': [new_row[3]],
                    'Leverage 3': ["NaN"],
                    'Notional Cap 3': ["NaN"],
                    'Leverage 4': ["NaN"],
                    'Notional Cap 4': ["NaN"],
                    'Leverage 5': ["NaN"],
                    'Notional Cap 5': ["NaN"],
                    'Leverage 6': ["NaN"],
                    'Notional Cap 6': ["NaN"],
                    'Leverage 7': ["NaN"],
                    'Notional Cap 7': ["NaN"],
                    'Leverage 8': ["NaN"],
                    'Notional Cap 8': ["NaN"],
                    'Leverage 9': ['NaN'],
                    'Notional Cap 9': ["NaN"],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
            elif len(new_row) == 2:
                new_info = pd.DataFrame({
                    'Symbol': [symbol],
                    'Funding Rate': [funding_rate],
                    'Leverage 1': [new_row[0]],
                    'Notional Cap 1': [new_row[1]],
                    'Leverage 2': ["NaN"],
                    'Notional Cap 2': ["NaN"],
                    'Leverage 3': ["NaN"],
                    'Notional Cap 3': ["NaN"],
                    'Leverage 4': ["NaN"],
                    'Notional Cap 4': ["NaN"],
                    'Leverage 5': ["NaN"],
                    'Notional Cap 5': ["NaN"],
                    'Leverage 6': ["NaN"],
                    'Notional Cap 6': ["NaN"],
                    'Leverage 7': ["NaN"],
                    'Notional Cap 7': ["NaN"],
                    'Leverage 8': ["NaN"],
                    'Notional Cap 8': ["NaN"],
                    'Leverage 9': ['NaN'],
                    'Notional Cap 9': ["NaN"],
                    'Leverage 10': ["NaN"],
                    'Notional Cap 10': ["NaN"],
                })
        if df is not None:
            df = pd.concat([df, new_info])
    return df
        # print("Added {}".format(symbol))

if __name__=='__main__':
    with st.expander('Binance'):
        with st.form('Binance Futures'):
            API_KEY=st.text_input('Enter readonly API key',type='password')
            API_SECRET=st.text_input('Enter readonly API Secret',type='password')

            st.markdown("###### :red[Disclaimer :-] Developer is not responsible for API key leak.though we dont store your credentials\n "
                        "however it's recommended to use readonly API keys created separately for this purpose")
            if not (API_SECRET is None and API_KEY is None):
                client = Client(API_KEY, API_SECRET)

            clicked=st.form_submit_button('Get binance Futures data')
            if 'download' not in st.session_state:
                st.session_state['download']=False

        if clicked:
            df_bin = get_data()
            csv = convert_df(df_bin)

            if st.session_state['download']==False:
                st.download_button(label="Download Binance Futures data as CSV",
                    data=convert_df(df_bin) if clicked else None,
                    file_name='Binance Futures_Data.csv',
                    mime='text/csv')

    # df.to_csv(r"C:\Users\princ\Downloads\NotionalandLeverageBrackets.csv")

