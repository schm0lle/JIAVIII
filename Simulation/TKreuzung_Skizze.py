import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.xlim = [-L-offset_x, L+offset_x]
ax.ylim = [-offset_y, L+offset_y]
ax.axis('equal')
ax.axis('off')

L = 1.0
offset_x = 0.5
offset_y = 0.25
P_u_l = [-L, L]
P_u_r = [L, L]
P_m_l = [-L, L/2]
P_m_ml = [-L/4, L/2]
P_m_mr= [L/4, L/2]
P_m_r = [L, L/2]
P_b_ml = [-L/4, 0]
P_b_mr = [L/4, 0]

ax.plot([P_u_l[0], P_u_r[0]], [P_u_l[1], P_u_r[1]], color='blue')
ax.plot([P_m_l[0], P_m_ml[0]], [P_m_l[1], P_m_ml[1]], color='blue')
ax.plot([P_m_r[0], P_m_mr[0]], [P_m_r[1], P_m_mr[1]], color='blue')
ax.plot([P_m_ml[0], P_b_ml[0]], [P_m_ml[1], P_b_ml[1]], color='blue')
ax.plot([P_m_mr[0], P_b_mr[0]], [P_m_mr[1], P_b_mr[1]], color='blue')

ax.text(P_u_l[0], (P_u_l[1] + P_m_l[1]) / 2, 'Straße A, Auto 1', horizontalalignment='center')
ax.text(P_u_r[0], (P_u_r[1] + P_m_r[1]) / 2, 'Straße C, Auto 3', horizontalalignment='center')
ax.text((P_b_ml[0] + P_b_mr[0]) / 2, P_b_ml[1] - offset_y, 'Straße B, Auto 2', horizontalalignment='center')

ax.text(0,L+offset_y, 'einspurig (in jede Richtung), rechts vor links', horizontalalignment='center')

fig.savefig('TKreuzung_Skizze.pdf')
plt.show()
