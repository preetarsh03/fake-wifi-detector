import pywifi
import time
import tkinter as tk
from tkinter import scrolledtext

def scan_wifi():
    output.delete(1.0, tk.END)
    output.insert(tk.END, "Scanning WiFi networks...\n")
    window.update()

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(4)

    results = iface.scan_results()

    if len(results) == 0:
        output.insert(tk.END, "No networks found\n")
        return

    for network in results:
        ssid = network.ssid
        signal = network.signal

        if signal < -80:
            risk = "HIGH RISK"
            tag = "high"
        elif signal < -60:
            risk = "MEDIUM RISK"
            tag = "medium"
        else:
            risk = "LOW RISK"
            tag = "low"

        output.insert(tk.END, f"WiFi: {ssid}\n")
        output.insert(tk.END, f"Signal: {signal}\n")
        output.insert(tk.END, f"Risk: {risk}\n", tag)
        output.insert(tk.END, "-----------------\n")

window = tk.Tk()
window.title("WiSafe - Fake WiFi Detector")
window.geometry("500x400")

scan_button = tk.Button(window, text="Scan WiFi", command=scan_wifi)
scan_button.pack(pady=10)

output = scrolledtext.ScrolledText(window, width=60, height=20)
output.pack()

output.tag_config("high", foreground="red")
output.tag_config("medium", foreground="orange")
output.tag_config("low", foreground="green")

window.mainloop()