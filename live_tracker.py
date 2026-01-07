#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║           LIVE NUMBER TRACKER - HACKER MODE ACTIVATED                    ║
║                    Made by Arpan | Cyberpunk Edition                      ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import psutil
import json
from datetime import datetime
from collections import deque
from threading import Thread, Lock
from typing import Dict, List

# Matrix effect constants
COLORS = {
    'GREEN': '\033[92m',
    'BRIGHT_GREEN': '\033[1;92m',
    'CYAN': '\033[96m',
    'RED': '\033[91m',
    'YELLOW': '\033[93m',
    'WHITE': '\033[97m',
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'DIM': '\033[2m',
}

class LiveNumberTracker:
    """Real-time number tracker with hacker vibes"""
    
    def __init__(self, max_history=50):
        self.numbers = deque(maxlen=max_history)
        self.timestamps = deque(maxlen=max_history)
        self.stats = {}
        self.lock = Lock()
        self.running = True
        self.session_start = time.time()
        
    def add_number(self, number: float, label: str = "Value"):
        """Add a number to tracker"""
        with self.lock:
            self.numbers.append(number)
            self.timestamps.append(datetime.now())
            self.update_stats()
            
    def update_stats(self):
        """Calculate real-time statistics"""
        if not self.numbers:
            return
            
        nums = list(self.numbers)
        self.stats = {
            'total': len(nums),
            'current': nums[-1] if nums else 0,
            'sum': sum(nums),
            'average': sum(nums) / len(nums) if nums else 0,
            'min': min(nums),
            'max': max(nums),
            'range': max(nums) - min(nums) if nums else 0,
        }
        
    def get_stats(self) -> Dict:
        """Get current statistics"""
        with self.lock:
            return self.stats.copy()


class HackerInterface:
    """Terminal hacker-style interface with Matrix vibes"""
    
    def __init__(self):
        self.tracker = LiveNumberTracker()
        self.width = 120
        self.height = 30
        
    def clear_screen(self):
        """Clear terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def matrix_rain(self, lines: int = 5):
        """Display Matrix-style falling characters"""
        chars = '日月火水木金土'
        for _ in range(lines):
            print(f"{COLORS['GREEN']}", end='')
            for _ in range(random.randint(10, 30)):
                print(random.choice(chars), end='', flush=True)
                time.sleep(0.01)
            print(COLORS['RESET'])
            
    def print_header(self):
        """Print hacker-style header"""
        header = f"""
{COLORS['BRIGHT_GREEN']}╔{'═' * (self.width - 2)}╗
║{' ' * (self.width - 2)}║
║{'LIVE NUMBER TRACKER - HACKER EDITION'.center(self.width - 2)}║
║{'Made by Arpan | Real-Time Analytics'.center(self.width - 2)}║
║{' ' * (self.width - 2)}║
╠{'═' * (self.width - 2)}╣{COLORS['RESET']}
"""
        print(header)
        
    def print_footer(self):
        """Print hacker-style footer"""
        footer = f"{COLORS['BRIGHT_GREEN']}╚{'═' * (self.width - 2)}╝{COLORS['RESET']}\n"
        print(footer)
        
    def print_stat_box(self, label: str, value, color: str = 'CYAN'):
        """Print a single stat box"""
        box = f"{COLORS[color]}[{label}]{COLORS['RESET']}: {COLORS['BRIGHT_GREEN']}{value}{COLORS['RESET']}"
        return box
        
    def display_dashboard(self):
        """Display main tracking dashboard"""
        while self.tracker.running:
            self.clear_screen()
            self.print_header()
            
            stats = self.tracker.get_stats()
            
            # Simulate real-time data
            self.simulate_data()
            stats = self.tracker.get_stats()
            
            # System info section
            print(f"{COLORS['YELLOW']}[SYSTEM STATUS]{COLORS['RESET']}")
            print(f"├─ CPU Usage: {COLORS['BRIGHT_GREEN']}{psutil.cpu_percent()}%{COLORS['RESET']}")
            print(f"├─ Memory Usage: {COLORS['BRIGHT_GREEN']}{psutil.virtual_memory().percent}%{COLORS['RESET']}")
            print(f"├─ Uptime: {COLORS['BRIGHT_GREEN']}{int(time.time() - self.tracker.session_start)}s{COLORS['RESET']}")
            print(f"└─ Process Count: {COLORS['BRIGHT_GREEN']}{len(psutil.pids())}{COLORS['RESET']}")
            
            print()
            print(f"{COLORS['YELLOW']}[TRACKING ANALYTICS]{COLORS['RESET']}")
            
            if stats:
                print(f"├─ {self.print_stat_box('Total Values', stats.get('total', 0))}")
                print(f"├─ {self.print_stat_box('Current Value', f\"{stats.get('current', 0):.2f}\", 'GREEN')}")
                print(f"├─ {self.print_stat_box('Sum', f\"{stats.get('sum', 0):.2f}\", 'CYAN')}")
                print(f"├─ {self.print_stat_box('Average', f\"{stats.get('average', 0):.2f}\", 'GREEN')}")
                print(f"├─ {self.print_stat_box('Min', f\"{stats.get('min', 0):.2f}\", 'RED')}")
                print(f"├─ {self.print_stat_box('Max', f\"{stats.get('max', 0):.2f}\", 'RED')}")
                print(f"└─ {self.print_stat_box('Range', f\"{stats.get('range', 0):.2f}\", 'YELLOW')}")
            
            print()
            print(f"{COLORS['YELLOW']}[RECENT ACTIVITY LOG]{COLORS['RESET']}")
            
            # Display last 5 numbers
            recent = list(self.tracker.numbers)[-5:]
            for i, num in enumerate(recent, 1):
                ts = list(self.tracker.timestamps)[-5:][i-1]
                print(f"├─ [{i}] {COLORS['BRIGHT_GREEN']}{num:.4f}{COLORS['RESET']} @ {ts.strftime('%H:%M:%S')}")
            
            print()
            print(f"{COLORS['CYAN']}[Status]{COLORS['RESET']}: {COLORS['BRIGHT_GREEN']}ACTIVE{COLORS['RESET']} | {COLORS['CYAN']}[Mode]{COLORS['RESET']}: {COLORS['BRIGHT_GREEN']}REAL-TIME{COLORS['RESET']}")
            
            self.print_footer()
            
            time.sleep(1)
            
    def simulate_data(self):
        """Simulate real-time number generation"""
        base = random.gauss(100, 15)
        noise = random.uniform(-5, 5)
        value = base + noise
        self.tracker.add_number(max(0, value))
        
    def start(self):
        """Start the tracker"""
        try:
            self.display_dashboard()
        except KeyboardInterrupt:
            self.shutdown()
            
    def shutdown(self):
        """Shutdown tracker"""
        self.tracker.running = False
        self.clear_screen()
        print(f"{COLORS['RED']}[SHUTDOWN]{COLORS['RESET']}: System going dark...")
        print(f"{COLORS['BRIGHT_GREEN']}[GOODBYE]{COLORS['RESET']}: Made with ❤️ by Arpan")
        time.sleep(1)
        sys.exit(0)


if __name__ == '__main__':
    tracker = HackerInterface()
    tracker.start()
