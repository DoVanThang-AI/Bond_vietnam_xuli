import numpy as np

def evaluate_bond(bond_price, face_value, coupon_rate, ytm, years_to_maturity, coupon_frequency):
    # Tính toán số lần trả coupon trong toàn bộ thời gian đáo hạn
    total_coupon_payments = years_to_maturity * coupon_frequency
    
    # Tính toán lượng tiền trả coupon trong một kỳ
    coupon_payment = (coupon_rate * face_value) / coupon_frequency
    
    # Tính toán danh sách các lợi tức (coupon) theo từng kỳ
    coupon_payments = np.full(total_coupon_payments, coupon_payment)
    
    # Tính toán lượng tiền trả về (face value) tại thời điểm đáo hạn
    final_payment = face_value
    
    # Tính toán danh sách các giá trị hiện tại của lợi tức và giá trị trả về
    present_values = coupon_payments / ((1 + ytm / coupon_frequency) ** np.arange(1, total_coupon_payments + 1))  
    present_values[-1] += final_payment / ((1 + ytm / coupon_frequency) ** total_coupon_payments)
    
    # Tính toán tổng giá trị hiện tại của trái phiếu
    present_value = np.sum(present_values)
    
    # Đánh giá trái phiếu dựa trên giá trị hiện tại
    if bond_price < present_value:
        return f"Trái phiếu định giá thấp hơn giá trị hiện tại:{present_value}"
    elif bond_price > present_value:
        return f"Trái phiếu định giá cao hơn giá trị hiện tại :{present_value}"
    else:
        return "Trái phiếu định giá gần bằng giá trị hiện tại"

# Ví dụ sử dụng hàm evaluate_bond
bond_price = 91903
face_value = 100000
coupon_rate = 0.073
ytm = 0.1021
years_to_maturity = 3
coupon_frequency = 2

evaluation = evaluate_bond(bond_price, face_value, coupon_rate, ytm, years_to_maturity, coupon_frequency)
print(evaluation)
