from imports import *
def Coupon_rate_bond(face_vl, annual_rate, per_term_year):
  annual_rate = annual_rate
  coupon = (annual_rate*face_vl)/(per_term_year*face_vl)
  return coupon

def cal_period_bond(data,col1,col2):
  data[col1] = pd.to_datetime(data[col1])
  data[col2] = pd.to_datetime(data[col2])
  return data[col1].dt.year - data[col2].dt.year



def market_prices(face_value, coupon_rate, coupon_freq, maturity):
    coupon_rate = coupon_rate/100
    num_payments = maturity * coupon_freq
    coupon_payment = (coupon_rate / coupon_freq) * face_value
    pv = 0
    for i in range(1, num_payments):
        pv += coupon_payment / ((1 + coupon_rate/coupon_freq) ** i)
    pv += face_value / ((1 + coupon_rate/coupon_freq) ** num_payments)
    return round(pv,1)
def Yield_to_marturity(market_price, face_value, years_to_maturity,per_time, annual_coupon_rate):
    annual_coupon_rate = annual_coupon_rate/100
    periods = years_to_maturity * per_time  # Assume semi-annual coupon payments
    coupon_payment = face_value * annual_coupon_rate / per_time
    dt = np.linspace(0.5, periods/per_time, periods)
    cashflows = np.full_like(dt, coupon_payment)
    cashflows[-1] += face_value  # Add face value to the final cashflow
    def f(y):
        return np.sum(cashflows / (1 + y / per_time) ** dt) - market_price
    return newton(f, 0.05) * per_time  # Return the semi-annual yield to maturity

def Modified_duration(face_vl,coupon,Yield,Time,per_time):
    '''
    face_vl: mệnh giá
    coupond: lãi suát hàng năm
    Yield: YTM
    Time: thời gian đáo hạn
    per_time: tấn suất đá
    '''
    cal = (1+(Yield/per_time)/100)
    coupon_payment = [(coupon/per_time)/100*face_vl]*(Time*per_time-1)+[(coupon/per_time)/100*face_vl+face_vl]
    coupon_payment
    total_payment = Time*per_time
    periods = np.arange(1,total_payment+1)
    d_cp = []
    pv_total=0
    total = 0
    for c,p in zip(coupon_payment,periods):
        tmp = [c / (cal**p)]
        for t in tmp:
            total +=t
    total_dcp = total
    for c,p in zip(coupon_payment,periods):
        tmp = [c / (cal**p)]
        for t in tmp:
            total +=t
            pv_total_dcp = [t*p/total_dcp]
            for i in pv_total_dcp:
                pv_total+=i

    Duration = pv_total/per_time
    Modified_Duration = Duration / (1+(Yield/per_time)/100)
    return Modified_Duration



TP_DN = pd.read_excel(r'D:\DATA\HOC_TAP\DO AN\Web_app\data\TRAIPHIEUDOANHNGHIEP_TECH.xlsx')
TP_DN = TP_DN.rename(columns={'Thời gian ĐT (tháng)':'TG giữ đến đáo hạn'})


TP_DN['Kỳ hạn trái phiếu'] = cal_period_bond(TP_DN,'Ngày đáo hạn','Ngày phát hành')
TP_DN['Lãi suất'] = TP_DN['Lãi suất'].map(lambda x : x*100)
TP_DN['Coupon_rate'] = TP_DN.apply(lambda x : Coupon_rate_bond(x['mệnh giá'],x['Lãi suất'],x['tần số trả lãi']),axis=1)

TP_DN['Market_price'] =TP_DN.apply(lambda x : market_prices(x['mệnh giá'],x['Lãi suất'],x['tần số trả lãi'],x['Kỳ hạn trái phiếu']),axis=1)
TP_DN['YTM'] = TP_DN.apply(lambda x : Yield_to_marturity(x['Market_price'],x['mệnh giá'],x['Kỳ hạn trái phiếu'],x['tần số trả lãi'],x['Coupon_rate']),axis=1)
TP_DN['Modified_duration']=TP_DN.apply(lambda x :Modified_duration(x['mệnh giá'],x['Lãi suất'],x['YTM'],x['Kỳ hạn trái phiếu'],x['tần số trả lãi']),axis=1 )
laisuat  = pd.DataFrame(TP_DN.groupby(['Lãi suất','Tổ chức phát hành'])['Lãi suất'].count()).rename(columns={'Lãi suất':'count'}).reset_index()

modified = TP_DN[['Modified_duration','Lãi suất','Tổ chức phát hành']]
df_modified =modified.groupby(['Tổ chức phát hành'])[['Modified_duration','Lãi suất']].mean().reset_index()

Data_table = TP_DN[['Mã TP','Lãi suất','Ngày phát hành','Ngày đáo hạn','mệnh giá','Market_price','YTM', 'Modified_duration']]