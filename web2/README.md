# Wisp WASM Web Runner

This directory contains the minimal setup to run Wisp WebAssembly in a web browser using the proper WASI implementation from the main web directory.

## Prerequisites

1. Build the Wisp WASM module first:
   ```bash
   cd ../core
   zig build
   ```
   This will generate `zig-out/bin/wisp.wasm`

## Running

### Option 1: Python Server (Recommended)
```bash
python3 serve.py
```

### Option 2: Node.js Server
```bash
node serve.js
```

### Option 3: Any HTTP Server
You can use any HTTP server that serves the current directory, but make sure it:
- Serves `.wasm` files with `application/wasm` MIME type
- Sets CORS headers for cross-origin isolation
- Supports ES6 modules

## Usage

1. Start one of the servers above
2. Open `http://localhost:8000` in your browser
3. The page will automatically load the Wisp WASM module
4. Enter Wisp code in the textarea (default example: `(+ 1 2 3)`) and click "Run"
5. Results will appear in the output area

## Files

- `index.html` - Main HTML page with proper Wisp WASM integration
- `wasi.js` - WASI implementation (copied from ../web/wasi.js)
- `wisp.js` - Wisp JavaScript interface (copied from ../web/wisp.js)
- `lib/idom.js` - DOM manipulation library dependency
- `serve.py` - Python HTTP server with proper WASM/CORS support
- `serve.js` - Node.js HTTP server alternative
- `package.json` - Node.js package configuration
- `README.md` - This file

## Features

- Full WASI implementation with proper file system stubs
- Complete Wisp JavaScript API integration
- Error handling and output capture
- ES6 module support
- Cross-origin isolation for WASM security

## Notes

- Uses the same WASI implementation as the main Wisp web interface
- Provides proper Wisp evaluation with `read()` and `eval()` functions
- Console output is captured and displayed in the web interface
- Modern browsers require HTTPS or localhost for SharedArrayBuffer and WASM features
- Check browser console for detailed debugging information