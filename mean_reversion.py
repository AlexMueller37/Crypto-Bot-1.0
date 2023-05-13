def mean_reversion(closes, in_position):
    import talib
    import numpy as np

    BBANDS_PERIOD = 20
    STD_DEV = 2

    if len(closes) > BBANDS_PERIOD:
            closes = np.array(closes)

            upper_band, middle_band, lower_band = talib.BBANDS(closes, timeperiod=BBANDS_PERIOD, nbdevup=STD_DEV, nbdevdn=STD_DEV, matype=talib.MA_Type.SMA)
            
            last_close = closes[-1]
            last_upper_band = upper_band[-1]
            last_middle_band = middle_band[-1]
            last_lower_band = lower_band[-1]

            print('======================================')
            print(f'upper band = {last_upper_band}')
            print(f'middle band = {last_middle_band}')
            print(f'lower band = {last_lower_band}')
            print(f'last close = {last_close}')
            print('======================================')
            
            if (last_close <= last_lower_band):
                if in_position:
                    print('Nothing')
                    return 'no action'
                else:
                    print('Buying')
                    return 'buy'
                
            if (last_close >= last_upper_band):
                if in_position:
                    print('Selling')
                    return 'sell'
                else:
                    print('Nothing')
                    return 'no action'      