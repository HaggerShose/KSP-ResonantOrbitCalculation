import math

K = 2500000  # Maximum com range of antenna
N = 3  # Number of desired satellites
MU = 65138398000  # Gravitational parameter of specified body
R = 200000  # Radius of specified body

sin_term = math.sin(math.radians(180 / N))


def format_seconds(seconds):
    days = int(seconds // 21600)
    hours = int(seconds % 21600) // 3600
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{days}d {hours:02d}h {minutes:02d}m {secs:05.3f}s"


def sma_z(k):
    sma_z_value = (k / 2) / sin_term
    return sma_z_value


def ap_pe_z(k):
    ap_z_value = sma_z(k) - R
    return ap_z_value


def t_z(k, mu):
    numerator = (k / 2) / sin_term
    t_zi = 2 * math.pi * math.sqrt((numerator**3) / mu)
    return t_zi


def sma_tl(k, n):
    cube_root_term = ((n - 1) ** 2 / n**2) ** (1 / 3)
    sma_tl_value = cube_root_term * (k / 2) / sin_term
    return sma_tl_value


def r_petl(k, n):
    cube_root_n_minus_1_squared = (n - 1) ** (2 / 3)
    cube_root_n_squared = n ** (2 / 3)
    r_petl_value = (
        (k / 2)
        * (2 * cube_root_n_minus_1_squared - cube_root_n_squared)
        / (cube_root_n_squared * sin_term)
    )
    return r_petl_value


def petl(k, n):
    petl_value = r_petl(k, n) - R
    return petl_value


def t_tl(k, n, mu):
    t_tl_value = 2 * math.pi * ((n - 1) / n) * math.sqrt((k / 2) ** 3 / (mu * sin_term**3))
    return t_tl_value


def delta_v_tl(k, n, mu):
    left_term = math.sqrt((2 * mu * sin_term) / k)
    cube_root_n_term_squared = (n / (n - 1)) ** (2 / 3)
    delta_v_tl_value = left_term * (1 - (math.sqrt(2 - cube_root_n_term_squared)))
    return delta_v_tl_value


def sma_th(k, n):
    cube_root_term = ((n + 1) ** 2 / n**2) ** (1 / 3)
    sma_th_value = cube_root_term * (k / 2) / sin_term
    return sma_th_value


def r_apth(k, n):
    cube_root_n_plus_1_squared = (n + 1) ** (2 / 3)
    cube_root_n_squared = n ** (2 / 3)
    r_apth_value = (
        (k / 2)
        * (2 * cube_root_n_plus_1_squared - cube_root_n_squared)
        / (cube_root_n_squared * sin_term)
    )
    return r_apth_value


def apth(k, n):
    apth_value = r_apth(k, n) - R
    return apth_value


def t_th(k, n, mu):
    t_th_value = 2 * math.pi * ((n + 1) / n) * math.sqrt((k / 2) ** 3 / (mu * sin_term**3))
    return t_th_value


def delta_v_th(k, n, mu):
    left_term = math.sqrt((2 * mu * sin_term) / k)
    cube_root_n_term_squared = (n / (n + 1)) ** (2 / 3)
    delta_v_th_value = left_term * ((math.sqrt(2 - cube_root_n_term_squared)) - 1)
    return delta_v_th_value


def sma_maxcom(k, n):
    cot_term = 1 / math.tan(math.radians(180 / n))
    sma_maxcom_value = (k / 2) * (cot_term + math.sqrt(3))
    return sma_maxcom_value


def ap_pe_maxcom(k, n):
    ap_pe_maxcom_value = sma_maxcom(k, n) - R
    return ap_pe_maxcom_value


def sma_mincom(k):
    sma_mincom_value = k * math.sqrt(1 - 1 / (2 * sin_term) ** 2)
    return sma_mincom_value


def ap_pe_mincom(k):
    ap_pe_mincom_value = sma_mincom(k) - R
    return ap_pe_mincom_value


print(f"{sma_z(K):,.3f} m = SMA_z".replace(",", " "))
print(f"{ap_pe_z(K):,.3f} m = Ap_z".replace(",", " "))
print(f"{format_seconds(t_z(K, MU))} = T_z\n")

print(f"{sma_tl(K, N):,.3f} m = SMA_tl".replace(",", " "))
print(f"{r_petl(K, N):,.3f} m = R_petl".replace(",", " "))
print(f"{petl(K, N):,.3f} m = Petl".replace(",", " "))
print(f"{format_seconds(t_tl(K, N, MU))} = T_tl")
print(f"{delta_v_tl(K, N, MU):,.3f} m/s = Delta_v_tl\n")

print(f"{sma_th(K, N):,.3f} m = SMA_th".replace(",", " "))
print(f"{r_apth(K, N):,.3f} m = R_apth".replace(",", " "))
print(f"{apth(K, N):,.3f} m = Apth".replace(",", " "))
print(f"{format_seconds(t_th(K, N, MU))} = T_th")
print(f"{delta_v_th(K, N, MU):,.3f} m/s = Delta_v_th\n")

print(f"{sma_maxcom(K, N):,.3f} m = SMA_maxcom".replace(",", " "))
print(f"{ap_pe_maxcom(K, N):,.3f} m = Ap_pe_maxcom\n".replace(",", " "))

print(f"{sma_mincom(K):,.3f} m = SMA_mincom".replace(",", " "))
print(f"{ap_pe_mincom(K):,.3f} m = Ap_pe_mincom\n".replace(",", " "))
