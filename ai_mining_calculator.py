import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import math
import webbrowser
import csv
import os

class AIMiningCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Mining Profitability Calculator")
        self.root.geometry("650x750")
        self.root.resizable(True, True)
        
        # GPU power consumption database (in watts)
        self.gpu_power_data = {
            "Custom/Manual Input": 0,
            # NVIDIA RTX 5 Series (Estimated)
            "NVIDIA RTX 5090": 500,
            "NVIDIA RTX 5080": 350,
            "NVIDIA RTX 5070 Ti": 300,
            "NVIDIA RTX 5070": 250,
            "NVIDIA RTX 5060 Ti": 180,
            "NVIDIA RTX 5060": 130,
            # NVIDIA RTX 4 Series
            "NVIDIA RTX 4090": 450,
            "NVIDIA RTX 4080 Super": 320,
            "NVIDIA RTX 4080": 320,
            "NVIDIA RTX 4070 Ti Super": 285,
            "NVIDIA RTX 4070 Ti": 285,
            "NVIDIA RTX 4070 Super": 220,
            "NVIDIA RTX 4070": 200,
            "NVIDIA RTX 4060 Ti": 165,
            "NVIDIA RTX 4060": 115,
            # NVIDIA RTX 3 Series
            "NVIDIA RTX 3090 Ti": 450,
            "NVIDIA RTX 3090": 350,
            "NVIDIA RTX 3080 Ti": 350,
            "NVIDIA RTX 3080": 320,
            "NVIDIA RTX 3070 Ti": 290,
            "NVIDIA RTX 3070": 220,
            "NVIDIA RTX 3060 Ti": 200,
            "NVIDIA RTX 3060": 170,
            "NVIDIA RTX 3050": 130,
            # NVIDIA RTX 2 Series
            "NVIDIA RTX 2080 Ti": 250,
            "NVIDIA RTX 2080 Super": 250,
            "NVIDIA RTX 2080": 215,
            "NVIDIA RTX 2070 Super": 215,
            "NVIDIA RTX 2070": 175,
            "NVIDIA RTX 2060 Super": 175,
            "NVIDIA RTX 2060": 160,
            # NVIDIA GTX Series
            "NVIDIA GTX 1080 Ti": 250,
            "NVIDIA GTX 1080": 180,
            "NVIDIA GTX 1070 Ti": 180,
            "NVIDIA GTX 1070": 150,
            "NVIDIA GTX 1060 6GB": 120,
            "NVIDIA GTX 1060 3GB": 120,
            # AMD RX 9 Series (Estimated)
            "AMD RX 9900 XTX": 400,
            "AMD RX 9900 XT": 350,
            "AMD RX 9800 XT": 300,
            "AMD RX 9700 XT": 250,
            "AMD RX 9600 XT": 200,
            "AMD RX 9600": 170,
            # AMD RX 7 Series
            "AMD RX 7900 XTX": 355,
            "AMD RX 7900 XT": 315,
            "AMD RX 7800 XT": 263,
            "AMD RX 7700 XT": 245,
            "AMD RX 7600 XT": 190,
            "AMD RX 7600": 165,
            # AMD RX 6 Series
            "AMD RX 6950 XT": 335,
            "AMD RX 6900 XT": 300,
            "AMD RX 6800 XT": 300,
            "AMD RX 6800": 250,
            "AMD RX 6700 XT": 230,
            "AMD RX 6600 XT": 160,
            "AMD RX 6600": 132,
            "AMD RX 6500 XT": 107,
            "AMD RX 6400": 53,
            # AMD RX 5 Series
            "AMD RX 5700 XT": 225,
            "AMD RX 5700": 180,
            "AMD RX 5600 XT": 150,
            "AMD RX 5500 XT": 130,
            # AMD RX 500 Series
            "AMD RX 580": 185,
            "AMD RX 570": 150,
            "AMD RX 560": 80,
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create main frame (no scrolling for main window)
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, text="AI Mining Profitability Calculator", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Currency frame (moved to top)
        currency_frame = ttk.LabelFrame(main_frame, text="Currency Settings", padding="10")
        currency_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Currency note
        note_label = ttk.Label(currency_frame, text="Select your currency - all inputs and outputs will use this currency", 
                              font=("Arial", 9), foreground="blue")
        note_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 5))
        
        # Currency selection
        ttk.Label(currency_frame, text="Currency:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.currency_var = tk.StringVar(value="USD")
        currency_combo = ttk.Combobox(currency_frame, textvariable=self.currency_var, 
                                     values=["USD", "EUR", "GBP", "AUD", "CNY", "JPY", "INR", "KRW", "RUB"], 
                                     state="readonly", width=10)
        currency_combo.grid(row=1, column=1, sticky=tk.W, pady=2)
        currency_combo.bind("<<ComboboxSelected>>", self.on_currency_changed)
        
        # Exchange rate
        ttk.Label(currency_frame, text="Exchange Rate (USD to selected currency):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.exchange_rate_var = tk.StringVar(value="1.0")
        ttk.Entry(currency_frame, textvariable=self.exchange_rate_var, width=15).grid(row=2, column=1, sticky=tk.W, pady=2)
        
        # Exchange rate button
        exchange_button = ttk.Button(currency_frame, text="Check Exchange Rates", 
                                   command=self.open_exchange_rates)
        exchange_button.grid(row=2, column=2, sticky=tk.W, padx=(10, 0), pady=2)
        
        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Input Parameters", padding="10")
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        # GPU Selection
        ttk.Label(input_frame, text="GPU Selection:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.gpu_var = tk.StringVar(value="Custom/Manual Input")
        self.gpu_combo = ttk.Combobox(input_frame, textvariable=self.gpu_var, 
                                     values=list(self.gpu_power_data.keys()), 
                                     state="readonly", width=30)
        self.gpu_combo.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E, pady=2)
        self.gpu_combo.bind("<<ComboboxSelected>>", self.on_gpu_selected)
        
        # Number of GPUs
        ttk.Label(input_frame, text="Number of GPUs:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.num_gpus_var = tk.StringVar(value="1")
        gpu_entry = ttk.Entry(input_frame, textvariable=self.num_gpus_var, width=15)
        gpu_entry.grid(row=1, column=1, sticky=tk.W, pady=2)
        gpu_entry.bind("<KeyRelease>", self.on_gpu_count_changed)
        
        # Power Consumption
        ttk.Label(input_frame, text="Total Power Consumption (kW):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.power_var = tk.StringVar(value="0.300")
        self.power_entry = ttk.Entry(input_frame, textvariable=self.power_var, width=15)
        self.power_entry.grid(row=2, column=1, sticky=tk.W, pady=2)
        ttk.Label(input_frame, text="(Total system power under load)").grid(row=2, column=2, sticky=tk.W, pady=2)
        
        # Hardware Cost
        ttk.Label(input_frame, text="Hardware Cost:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.hardware_cost_var = tk.StringVar(value="1500")
        ttk.Entry(input_frame, textvariable=self.hardware_cost_var, width=15).grid(row=3, column=1, sticky=tk.W, pady=2)
        self.hardware_cost_label = ttk.Label(input_frame, text="(in selected currency)")
        self.hardware_cost_label.grid(row=3, column=2, sticky=tk.W, pady=2)
        
        # AI Mining Income
        ttk.Label(input_frame, text="AI Mining Income ($/hour):").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.income_var = tk.StringVar(value="0.50")
        ttk.Entry(input_frame, textvariable=self.income_var, width=15).grid(row=4, column=1, sticky=tk.W, pady=2)
        ttk.Label(input_frame, text="(always in USD from platform)").grid(row=4, column=2, sticky=tk.W, pady=2)
        
        # Platform Cut
        ttk.Label(input_frame, text="Platform Cut (%):").grid(row=5, column=0, sticky=tk.W, pady=2)
        self.cut_var = tk.StringVar(value="10")
        ttk.Entry(input_frame, textvariable=self.cut_var, width=15).grid(row=5, column=1, sticky=tk.W, pady=2)
        
        # Electricity pricing frame
        elec_frame = ttk.LabelFrame(main_frame, text="Electricity Pricing", padding="10")
        elec_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Simple vs Time-of-Use pricing
        self.pricing_type = tk.StringVar(value="simple")
        ttk.Radiobutton(elec_frame, text="Simple Pricing", variable=self.pricing_type, 
                       value="simple", command=self.toggle_pricing_type).grid(row=0, column=0, sticky=tk.W)
        ttk.Radiobutton(elec_frame, text="Time-of-Use Pricing", variable=self.pricing_type, 
                       value="tou", command=self.toggle_pricing_type).grid(row=0, column=1, sticky=tk.W)
        
        # Simple pricing
        ttk.Label(elec_frame, text="Electricity Cost (per kWh):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.elec_cost_var = tk.StringVar(value="0.12")
        self.elec_cost_entry = ttk.Entry(elec_frame, textvariable=self.elec_cost_var, width=15)
        self.elec_cost_entry.grid(row=1, column=1, sticky=tk.W, pady=2)
        self.elec_cost_label = ttk.Label(elec_frame, text="(in selected currency)")
        self.elec_cost_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        
        # Time-of-Use pricing (initially hidden)
        self.tou_frame = ttk.Frame(elec_frame)
        
        ttk.Label(self.tou_frame, text="Off-Peak Price (per kWh):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.off_peak_price_var = tk.StringVar(value="0.08")
        ttk.Entry(self.tou_frame, textvariable=self.off_peak_price_var, width=15).grid(row=0, column=1, sticky=tk.W, pady=2)
        self.off_peak_label = ttk.Label(self.tou_frame, text="(in selected currency)")
        self.off_peak_label.grid(row=0, column=2, sticky=tk.W, pady=2)
        
        ttk.Label(self.tou_frame, text="On-Peak Price (per kWh):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.on_peak_price_var = tk.StringVar(value="0.18")
        ttk.Entry(self.tou_frame, textvariable=self.on_peak_price_var, width=15).grid(row=1, column=1, sticky=tk.W, pady=2)
        self.on_peak_label = ttk.Label(self.tou_frame, text="(in selected currency)")
        self.on_peak_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        
        ttk.Label(self.tou_frame, text="Off-Peak Hours per Day:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.off_peak_hours_var = tk.StringVar(value="16")
        ttk.Entry(self.tou_frame, textvariable=self.off_peak_hours_var, width=15).grid(row=2, column=1, sticky=tk.W, pady=2)
        ttk.Label(self.tou_frame, text="(On-peak calculated automatically)").grid(row=2, column=2, sticky=tk.W, pady=2)
        
        # Calculate button
        calc_button = ttk.Button(main_frame, text="Calculate Profitability", 
                                command=self.calculate, style="Accent.TButton")
        calc_button.pack(pady=10)
        
        # Results frame with fixed height
        self.results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        self.results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Save buttons frame
        save_frame = ttk.Frame(self.results_frame)
        save_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(save_frame, text="Save as TXT", command=self.save_as_txt).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(save_frame, text="Save as CSV", command=self.save_as_csv).pack(side=tk.LEFT)
        
        # Results text widget with scrollbar (only results area scrollable)
        results_container = ttk.Frame(self.results_frame)
        results_container.pack(fill=tk.BOTH, expand=True)
        
        self.results_text = tk.Text(results_container, height=10, width=70, 
                                   font=("Consolas", 10), wrap=tk.WORD)
        results_scrollbar = ttk.Scrollbar(results_container, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=results_scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure grid weights
        input_frame.columnconfigure(1, weight=1)
        elec_frame.columnconfigure(1, weight=1)
        currency_frame.columnconfigure(1, weight=1)
        
        # Store results for saving
        self.last_results = None
        
        # Initialize currency symbols
        self.currency_symbols = {
            "USD": "$", "EUR": "€", "GBP": "£", "AUD": "A$", 
            "CNY": "¥", "JPY": "¥", "INR": "₹", "KRW": "₩", "RUB": "₽"
        }
        
    def on_currency_changed(self, event=None):
        """Update labels when currency changes"""
        currency = self.currency_var.get()
        if currency == "USD":
            self.exchange_rate_var.set("1.0")
    
    def get_currency_symbol(self):
        """Get the symbol for the selected currency"""
        return self.currency_symbols.get(self.currency_var.get(), "$")
        
    def open_exchange_rates(self):
        webbrowser.open("https://www.google.com/search?q=dollar+exchange+rate")
        
    def on_gpu_selected(self, event=None):
        self.update_power_consumption()
        
    def on_gpu_count_changed(self, event=None):
        self.update_power_consumption()
        
    def update_power_consumption(self):
        try:
            selected_gpu = self.gpu_var.get()
            num_gpus_str = self.num_gpus_var.get().strip()
            if not num_gpus_str:
                return
            num_gpus = int(num_gpus_str)
            
            if selected_gpu in self.gpu_power_data and selected_gpu != "Custom/Manual Input":
                gpu_power_watts = self.gpu_power_data[selected_gpu]
                # Add ~100W for system overhead (CPU, motherboard, etc.)
                total_power_watts = (gpu_power_watts * num_gpus) + 100
                total_power_kw = total_power_watts / 1000
                self.power_var.set(f"{total_power_kw:.3f}")
        except ValueError:
            pass  # Invalid number of GPUs, ignore
        
    def toggle_pricing_type(self):
        if self.pricing_type.get() == "simple":
            self.tou_frame.grid_remove()
            self.elec_cost_entry.grid(row=1, column=1, sticky=tk.W, pady=2)
            self.elec_cost_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        else:
            self.elec_cost_entry.grid_remove()
            self.elec_cost_label.grid_remove()
            self.tou_frame.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E, pady=10)
    
    def calculate(self):
        try:
            # Get input values
            power_kw = float(self.power_var.get())
            hardware_cost_local = float(self.hardware_cost_var.get())
            income_per_hour = float(self.income_var.get())  # Always in USD
            platform_cut = float(self.cut_var.get()) / 100
            exchange_rate = float(self.exchange_rate_var.get())
            currency_symbol = self.get_currency_symbol()
            
            # Convert local currency inputs to USD for calculations
            hardware_cost_usd = hardware_cost_local / exchange_rate
            
            # Calculate net income after platform cut
            net_income_per_hour = income_per_hour * (1 - platform_cut)
            
            # Calculate electricity costs (convert from local currency to USD)
            if self.pricing_type.get() == "simple":
                elec_cost_per_kwh_local = float(self.elec_cost_var.get())
                elec_cost_per_kwh_usd = elec_cost_per_kwh_local / exchange_rate
                elec_cost_per_hour_usd = power_kw * elec_cost_per_kwh_usd
                avg_elec_cost_per_hour_usd = elec_cost_per_hour_usd
            else:
                off_peak_price_local = float(self.off_peak_price_var.get())
                on_peak_price_local = float(self.on_peak_price_var.get())
                off_peak_hours = float(self.off_peak_hours_var.get())
                on_peak_hours = 24 - off_peak_hours
                
                # Convert to USD
                off_peak_price_usd = off_peak_price_local / exchange_rate
                on_peak_price_usd = on_peak_price_local / exchange_rate
                
                # Calculate weighted average electricity cost
                off_peak_cost = power_kw * off_peak_price_usd * off_peak_hours
                on_peak_cost = power_kw * on_peak_price_usd * on_peak_hours
                total_daily_elec_cost = off_peak_cost + on_peak_cost
                avg_elec_cost_per_hour_usd = total_daily_elec_cost / 24
            
            # Calculate profits (in USD)
            profit_per_hour_usd = net_income_per_hour - avg_elec_cost_per_hour_usd
            profit_per_24h_usd = profit_per_hour_usd * 24
            
            # Calculate hardware recovery time
            if profit_per_hour_usd > 0:
                recovery_hours = hardware_cost_usd / profit_per_hour_usd
                recovery_days = recovery_hours / 24
                recovery_months = recovery_days / 30.44  # Average month length
            else:
                recovery_hours = float('inf')
                recovery_days = float('inf')
                recovery_months = float('inf')
            
            # Calculate 5-year profitability with proper hardware cost accounting
            hours_per_year = 24 * 365.25
            yearly_profits_usd = []
            cumulative_profit_usd = -hardware_cost_usd  # Start with negative hardware cost
            
            for year in range(1, 6):
                yearly_gross_usd = profit_per_hour_usd * hours_per_year
                cumulative_profit_usd += yearly_gross_usd
                yearly_profits_usd.append(cumulative_profit_usd)
            
            # Display results
            self.display_results(
                power_kw, hardware_cost_usd, income_per_hour, platform_cut,
                net_income_per_hour, avg_elec_cost_per_hour_usd, profit_per_hour_usd,
                profit_per_24h_usd, recovery_days, recovery_months,
                yearly_profits_usd, exchange_rate, currency_symbol
            )
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for all fields.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def display_results(self, power_kw, hardware_cost_usd, income_per_hour, platform_cut,
                       net_income_per_hour, avg_elec_cost_per_hour_usd, profit_per_hour_usd,
                       profit_per_24h_usd, recovery_days, recovery_months,
                       yearly_profits_usd, exchange_rate, currency_symbol):
        
        self.results_text.delete(1.0, tk.END)
        
        # Convert values to selected currency for display
        def convert_currency(usd_amount):
            return usd_amount * exchange_rate
        
        def format_currency(amount):
            return f"{currency_symbol}{amount:,.2f}"
        
        results = f"""
AI MINING PROFITABILITY ANALYSIS
===============================================

INPUT PARAMETERS:
• Power Consumption: {power_kw:.3f} kW
• Hardware Cost: {format_currency(convert_currency(hardware_cost_usd))}
• Gross Income: ${income_per_hour:.4f}/hour (USD from platform)
• Platform Cut: {platform_cut*100:.1f}%
• Net Income: ${net_income_per_hour:.4f}/hour (USD)
• Electricity Cost: {format_currency(convert_currency(avg_elec_cost_per_hour_usd))}/hour

PROFITABILITY RESULTS:
===============================================
• Profit per Hour: {format_currency(convert_currency(profit_per_hour_usd))}
• Profit per 24 Hours: {format_currency(convert_currency(profit_per_24h_usd))}

HARDWARE RECOVERY:
"""
        
        if recovery_days == float('inf'):
            results += "• Hardware Recovery: NEVER (Operating at a loss)\n"
        else:
            results += f"• Hardware Recovery Time: {recovery_days:.1f} days ({recovery_months:.1f} months)\n"
        
        results += f"""
5-YEAR PROFITABILITY:
===============================================
"""
        
        # Check if profitable within 5 years
        if recovery_days > (5 * 365.25):
            results += "NOT PROFITABLE WITHIN 5 YEARS\n\n"
        
        for i, profit_usd in enumerate(yearly_profits_usd, 1):
            results += f"• Year {i} Total: {format_currency(convert_currency(profit_usd))}\n"
        
        results += f"""
SUMMARY:
===============================================
"""
        
        if profit_per_hour_usd > 0 and recovery_days <= (5 * 365.25):
            final_profit_usd = yearly_profits_usd[-1]  # 5-year total
            roi_percentage = (final_profit_usd / hardware_cost_usd) * 100
            results += f"• Status: ✓ PROFITABLE\n"
            results += f"• 5-Year ROI: {roi_percentage:.1f}%\n"
            results += f"• Break-even: {recovery_days:.1f} days\n"
        else:
            results += f"• Status: ✗ NOT PROFITABLE\n"
            if profit_per_hour_usd > 0:
                results += f"• Recovery time exceeds 5 years\n"
            else:
                results += f"• Daily Loss: {format_currency(convert_currency(abs(profit_per_24h_usd)))}\n"
            results += f"• Consider: Lower electricity costs or higher income rates\n"
        
        # Add efficiency metrics
        efficiency = (profit_per_hour_usd / net_income_per_hour) * 100 if net_income_per_hour > 0 else 0
        results += f"• Efficiency: {efficiency:.1f}% (after electricity costs)\n"
        
        self.results_text.insert(tk.END, results)
        
        # Store results for saving
        self.last_results = {
            'power_kw': power_kw,
            'hardware_cost_usd': hardware_cost_usd,
            'income_per_hour': income_per_hour,
            'platform_cut': platform_cut,
            'net_income_per_hour': net_income_per_hour,
            'avg_elec_cost_per_hour_usd': avg_elec_cost_per_hour_usd,
            'profit_per_hour_usd': profit_per_hour_usd,
            'profit_per_24h_usd': profit_per_24h_usd,
            'recovery_days': recovery_days,
            'recovery_months': recovery_months,
            'yearly_profits_usd': yearly_profits_usd,
            'exchange_rate': exchange_rate,
            'currency_symbol': currency_symbol,
            'text_results': results
        }
    
    def save_as_txt(self):
        if not self.last_results:
            messagebox.showwarning("Warning", "Please calculate results first before saving.")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Results as TXT"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.last_results['text_results'])
                messagebox.showinfo("Success", f"Results saved to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    
    def save_as_csv(self):
        if not self.last_results:
            messagebox.showwarning("Warning", "Please calculate results first before saving.")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="Save Results as CSV"
        )
        
        if filename:
            try:
                with open(filename, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    
                    # Header
                    writer.writerow(["AI Mining Profitability Analysis"])
                    writer.writerow([])
                    
                    # Input parameters
                    writer.writerow(["INPUT PARAMETERS"])
                    writer.writerow(["Power Consumption (kW)", self.last_results['power_kw']])
                    writer.writerow(["Hardware Cost", self.last_results['hardware_cost_usd'] * self.last_results['exchange_rate']])
                    writer.writerow(["Gross Income per Hour (USD)", self.last_results['income_per_hour']])
                    writer.writerow(["Platform Cut (%)", self.last_results['platform_cut'] * 100])
                    writer.writerow(["Net Income per Hour (USD)", self.last_results['net_income_per_hour']])
                    writer.writerow(["Electricity Cost per Hour", self.last_results['avg_elec_cost_per_hour_usd'] * self.last_results['exchange_rate']])
                    writer.writerow([])
                    
                    # Results
                    writer.writerow(["PROFITABILITY RESULTS"])
                    writer.writerow(["Profit per Hour", self.last_results['profit_per_hour_usd'] * self.last_results['exchange_rate']])
                    writer.writerow(["Profit per 24 Hours", self.last_results['profit_per_24h_usd'] * self.last_results['exchange_rate']])
                    writer.writerow([])
                    
                    # Recovery
                    writer.writerow(["HARDWARE RECOVERY"])
                    if self.last_results['recovery_days'] == float('inf'):
                        writer.writerow(["Recovery Time", "NEVER (Operating at a loss)"])
                    else:
                        writer.writerow(["Recovery Time (days)", self.last_results['recovery_days']])
                        writer.writerow(["Recovery Time (months)", self.last_results['recovery_months']])
                    writer.writerow([])
                    
                    # 5-year profitability
                    writer.writerow(["5-YEAR PROFITABILITY"])
                    for i, profit_usd in enumerate(self.last_results['yearly_profits_usd'], 1):
                        writer.writerow([f"Year {i} Total", profit_usd * self.last_results['exchange_rate']])
                    
                messagebox.showinfo("Success", f"Results saved to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def main():
    root = tk.Tk()
    app = AIMiningCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()