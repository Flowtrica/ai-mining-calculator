# AI Mining Profitability Calculator

A comprehensive GUI application to calculate the profitability of AI mining operations using services like Salad.com, Vast.ai, and similar platforms. This calculator helps you determine if AI mining is profitable for your hardware setup, taking into account electricity costs, hardware expenses, and various pricing models.

![AI Mining Calculator Screenshot](https://github.com/Flowtrica/ai-mining-calculator/blob/main/apc.png)

## 🚀 Features

### 💰 **Comprehensive Profitability Analysis**
- **Multiple Time Periods**: Profit calculations per hour, day, and year
- **5-Year Projection**: Long-term profitability analysis with hardware cost recovery
- **Break-even Analysis**: Calculates exactly when you'll recover hardware costs
- **ROI Calculations**: Return on investment percentages and efficiency metrics

### 🌍 **Multi-Currency Support**
- **9 Major Currencies**: USD, EUR, GBP, AUD, CNY, JPY, INR, KRW, RUB
- **Smart Input**: Enter costs in your local currency, results display in chosen currency
- **Live Exchange Rates**: Built-in link to Google's exchange rate checker
- **Automatic Conversion**: All calculations handle currency conversion seamlessly

### ⚡ **Advanced Electricity Pricing**
- **Simple Pricing**: Flat-rate electricity costs
- **Time-of-Use Pricing**: Off-peak and on-peak rate support
- **Automatic Calculations**: On-peak hours calculated automatically
- **Local Currency Input**: Enter electricity costs in your preferred currency

### 🎮 **Extensive GPU Database**
- **70+ GPUs Supported**: NVIDIA RTX 5000, 4000, 3000, 2000 series and GTX cards
- **AMD Support**: RX 9000, 7000, 6000, 5000, and 500 series cards
- **Multi-GPU Setups**: Support for multiple GPU configurations
- **Automatic Power Calculation**: Total system power including overhead

### 💾 **Export Capabilities**
- **Save as TXT**: Human-readable format for sharing
- **Save as CSV**: Structured data for spreadsheet analysis
- **Complete Data Export**: All calculations and parameters included

### 🖥️ **User-Friendly Interface**
- **Clean GUI**: Professional tkinter interface with logical layout
- **Input Validation**: Error handling and helpful error messages
- **Scrollable Results**: Fixed input area with scrollable results section
- **Responsive Design**: Works well on different screen sizes

## 📋 Requirements

- **Python 3.7+** (Python 3.8+ recommended)
- **tkinter** (usually included with Python)
- **PyInstaller** (for creating executables)

## 🛠️ Installation & Usage

### Running from Source
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-mining-calculator.git
   cd ai-mining-calculator
   ```

2. **Run the application**:
   ```bash
   python ai_mining_calculator.py
   ```

### Using Pre-compiled Executables
Download the latest release for your operating system from the [Releases](https://github.com/yourusername/ai-mining-calculator/releases) page.

## 🔨 Compilation Instructions

### Prerequisites
Install PyInstaller for creating standalone executables:
```bash
pip install pyinstaller
```

### Windows Compilation
```bash
# Basic compilation
python -m PyInstaller --onefile --windowed ai_mining_calculator.py

# With custom name and icon (if you have an .ico file)
python -m PyInstaller --onefile --windowed --name "AI_Mining_Calculator" --icon=icon.ico ai_mining_calculator.py

# Advanced options for better compatibility
python -m PyInstaller --onefile --windowed --name "AI_Mining_Calculator" --add-data "*.py;." ai_mining_calculator.py
```

**Output**: `dist/AI_Mining_Calculator.exe` (or `dist/ai_mining_calculator.exe`)

### macOS Compilation
```bash
# Basic compilation
python -m PyInstaller --onefile --windowed ai_mining_calculator.py

# With custom name and icon (if you have an .icns file)
python -m PyInstaller --onefile --windowed --name "AI_Mining_Calculator" --icon=icon.icns ai_mining_calculator.py

# For better macOS integration
python -m PyInstaller --onefile --windowed --name "AI_Mining_Calculator" --osx-bundle-identifier com.yourname.aiminingcalc ai_mining_calculator.py
```

**Output**: `dist/AI_Mining_Calculator` (Unix executable)

**Note**: On macOS, you may need to allow the app in System Preferences > Security & Privacy if it's blocked.

### Linux Compilation
```bash
# Basic compilation
python3 -m PyInstaller --onefile --windowed ai_mining_calculator.py

# With custom name
python3 -m PyInstaller --onefile --windowed --name "AI_Mining_Calculator" ai_mining_calculator.py

# For distribution (includes more libraries)
python3 -m PyInstaller --onefile --windowed --name "AI_Mining_Calculator" --add-binary '/usr/lib/x86_64-linux-gnu/libtkinter*:.' ai_mining_calculator.py
```

**Output**: `dist/AI_Mining_Calculator` (Linux executable)

### Platform-Specific Notes

#### Windows
- The executable may be flagged by antivirus software (common with PyInstaller)
- Add an exception or use `--exclude-module` flags for unnecessary modules
- Consider code signing for professional distribution

#### macOS
- You may need to install tkinter separately: `brew install python-tk`
- For distribution, consider notarizing the app for Gatekeeper compatibility
- Use `--osx-bundle-identifier` for proper macOS integration

#### Linux
- Install tkinter if missing: `sudo apt-get install python3-tk` (Ubuntu/Debian)
- For other distributions: `sudo yum install tkinter` (CentOS/RHEL)
- The executable requires the same or compatible Linux distribution to run

### Troubleshooting Compilation

1. **Missing tkinter**: Install the python3-tk package for your system
2. **Large file size**: Use `--exclude-module` to remove unnecessary modules
3. **Slow startup**: Remove `--onefile` flag to create a folder instead of single file
4. **Import errors**: Use `--add-data` or `--add-binary` flags to include missing files

## 📖 How to Use

1. **Set Currency**: Choose your local currency and exchange rate
2. **Select GPU**: Pick your GPU from the dropdown or use manual input
3. **Enter Parameters**:
   - Number of GPUs in your system
   - Total power consumption (auto-calculated for known GPUs)
   - Hardware cost (in your currency)
   - AI mining income rate (in USD from platform)
   - Platform cut percentage
4. **Configure Electricity**:
   - Choose simple or time-of-use pricing
   - Enter rates in your local currency
5. **Calculate**: Click "Calculate Profitability"
6. **Review Results**: Analyze profit per hour/day/year and break-even time
7. **Export**: Save results as TXT or CSV for record-keeping

## 💡 Example Use Cases

- **Home Miners**: Calculate if your gaming PC can generate profit overnight
- **Small Farms**: Analyze multi-GPU setups with time-of-use electricity rates
- **International Users**: Compare profitability across different countries/currencies
- **Hardware Planning**: Determine if new GPU purchases are financially viable
- **Tax Planning**: Export annual profit projections for tax calculations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:

- Additional GPU models and power consumption data
- New currency support
- UI/UX improvements
- Bug fixes and performance optimizations
- Documentation improvements

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

## 📝 GPU Database

The calculator includes power consumption data for:
- **NVIDIA**: RTX 5000, 4000, 3000, 2000 series, GTX 1000 series
- **AMD**: RX 9000, 7000, 6000, 5000, 500 series

Power values include typical gaming/mining loads. The calculator adds ~100W system overhead automatically.

## ⚠️ Disclaimers

- **Power consumption values** are estimates based on typical specifications
- **Actual results** may vary based on specific hardware configurations, mining efficiency, and market conditions
- **This tool is for estimation purposes only** and should not be considered financial advice
- **Always verify** power consumption with actual measurements when possible
- **AI mining profitability** can change rapidly based on demand and competition

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- GPU power consumption data compiled from manufacturer specifications and community testing
- Exchange rate integration with Google's currency converter
- Built with Python's tkinter for cross-platform compatibility

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/ai-mining-calculator/issues) page
2. Create a new issue with detailed information about your problem
3. Include your operating system, Python version, and error messages

---

**Star ⭐ this repository if you find it helpful!**