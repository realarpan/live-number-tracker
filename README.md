# 🎯 LIVE NUMBER TRACKER - HACKER EDITION

```
╔═══════════════════════════════════════════════════════════════════════════╗
║           LIVE NUMBER TRACKER - HACKER MODE ACTIVATED                    ║
║                    Made by Arpan | Cyberpunk Edition                      ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

A sophisticated real-time number tracker with Matrix-inspired hacker vibes, featuring a cyberpunk terminal interface, live analytics dashboard, and comprehensive system monitoring capabilities.

## 🌟 Features

✅ **Real-Time Tracking** - Monitor numbers as they're generated in real-time  
✅ **Hacker Interface** - Matrix-style green terminal with cyberpunk aesthetics  
✅ **Live Analytics Dashboard** - View instant statistics and metrics  
✅ **System Monitoring** - CPU usage, memory, uptime, process count tracking  
✅ **Statistical Analysis** - Total, average, min, max, range calculations  
✅ **Activity Log** - Recent number entries with timestamps  
✅ **Thread-Safe Operations** - Concurrent data handling with locks  
✅ **Color-Coded Output** - Different colors for different data types  
✅ **Lightweight** - Minimal dependencies, fast performance  
✅ **Customizable** - Easy to modify and extend

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

```bash
git clone https://github.com/realarpan/live-number-tracker.git
cd live-number-tracker
pip install -r requirements.txt
```

## 🎮 Usage

### Basic Usage

```bash
python live_tracker.py
```

### What You'll See

The tracker displays:

1. **SYSTEM STATUS**
   - CPU Usage percentage
   - Memory Usage percentage
   - Current session uptime in seconds
   - Active process count

2. **TRACKING ANALYTICS**
   - Total Values: Count of tracked numbers
   - Current Value: Latest number added
   - Sum: Total of all numbers
   - Average: Mean value
   - Min: Minimum value
   - Max: Maximum value
   - Range: Difference between min and max

3. **RECENT ACTIVITY LOG**
   - Last 5 numbers tracked
   - Timestamp for each entry
   - Color-coded values

## 📊 Data Tracked

### Per-Number Metrics
- **Value**: The actual number
- **Timestamp**: When it was added (HH:MM:SS)
- **Color Coding**:
  - Green: Current and average values
  - Cyan: Total values and sums
  - Red: Minimum and maximum values
  - Yellow: Range values

### System Metrics
- **CPU Usage**: Current processor utilization
- **Memory Usage**: RAM consumption percentage
- **Uptime**: Time since tracker started
- **Process Count**: Active system processes

## 🔧 Configuration

Edit `live_tracker.py` to customize:

```python
# Maximum history size
max_history = 50  # Change to store more/fewer values

# Terminal dimensions
self.width = 120   # Dashboard width
self.height = 30   # Dashboard height

# Update interval
time.sleep(1)  # Change to update faster/slower
```

## 📁 Project Structure

```
live-number-tracker/
├── live_tracker.py       # Main tracker application
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎨 Color Scheme

| Color | Usage |
|-------|-------|
| Green | Current values, active status |
| Bright Green | Numerical values in output |
| Cyan | Data labels and headers |
| Red | Critical values (min/max) |
| Yellow | Section titles and range |
| White | System information |

## 💻 System Requirements

- **OS**: Linux, macOS, or Windows
- **Memory**: Minimal (< 50MB)
- **CPU**: Any modern processor
- **Terminal**: ANSI color support recommended

## 🧪 How It Works

1. **LiveNumberTracker Class**: Core tracking engine
   - Stores numbers with timestamps
   - Calculates real-time statistics
   - Thread-safe data operations

2. **HackerInterface Class**: Terminal UI
   - Renders dashboard
   - Simulates real-time data
   - Displays system metrics
   - Handles graceful shutdown

3. **Data Flow**:
   ```
   Data Generation → Add to Tracker → Calculate Stats → Display Dashboard → Repeat
   ```

## 📈 Performance

- **Update Frequency**: 1 second intervals
- **History Size**: 50 numbers default
- **Memory Usage**: < 1MB
- **CPU Usage**: < 1% idle

## 🛑 Exit

Press `Ctrl + C` to gracefully shutdown the tracker.

## 🔮 Future Enhancements

- [ ] Data export to CSV/JSON
- [ ] Graph visualization
- [ ] Custom data input
- [ ] Database storage
- [ ] Web dashboard
- [ ] Mobile app integration
- [ ] Advanced filtering
- [ ] Predictive analytics

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📜 License

MIT License - Feel free to use this project for any purpose!

## 👨‍💻 Author

**Arpan**
- GitHub: [@realarpan](https://github.com/realarpan)
- Made with ❤️ and cyberpunk vibes

## 🙏 Acknowledgments

- **psutil** - System and process utilities
- **Python** - Amazing programming language
- Matrix effect inspiration for the hacker aesthetics

## 📞 Support

If you encounter any issues:
1. Check that Python 3.8+ is installed
2. Verify all requirements are installed: `pip install -r requirements.txt`
3. Open an issue on GitHub

---

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                      MADE WITH ❤️ BY ARPAN                               ║
║              Real-Time Number Tracking with Cyberpunk Vibes              ║
╚═══════════════════════════════════════════════════════════════════════════╝
```
