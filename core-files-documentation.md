# Wisp Core Directory Files Documentation

This document describes the purpose and functionality of all files in the `wisp/core` directory, which contains the core implementation of the Wisp programming language interpreter written in Zig.

## Build and Configuration Files

### `build.zig`
Zig build configuration file that defines how to compile the Wisp interpreter. Sets up multiple build targets including native executables, WASM builds, and test configurations. Manages dependencies like the ziglyph Unicode library and configures exported symbols for WASM integration.

### `build.zig.zon`
Zig package configuration file that specifies project dependencies and their versions.

### `boot.zig`
Bootstrap program that creates the initial Wisp core image. Initializes a heap with base functionality, performs garbage collection, and saves the resulting core state to `boot.core` for fast startup.

### `boot.core`
Binary file containing the serialized Wisp core system state. This precompiled core includes base functions, macros, and system definitions, allowing the interpreter to start quickly without recompiling the base library.

## Main Entry Points

### `main.zig`
Primary entry point for the Wisp interpreter CLI. Handles command-line argument parsing and dispatches to various modes:
- `run`: Execute Wisp programs from files
- `repl`: Start interactive Read-Eval-Print Loop
- `eval`: Evaluate Wisp expressions from command line
- `core`: Generate boot core files
- `load`: Load saved core files
- `keygen`: Generate cryptographic keys

### `wasm.zig`
WebAssembly interface module that exports Wisp functionality for browser/WASM environments. Provides C-compatible API functions for JavaScript integration, memory management, and cross-platform execution.

## Core Language Implementation

### `wisp.zig`
Main module that re-exports core Wisp functionality. Serves as the central namespace for word types, heap management, and platform detection (browser vs native).

### `word.zig`
Fundamental data type system for Wisp. Defines the core Word type that represents all Lisp values, including:
- Integers, characters, symbols
- Cons cells (pairs)
- Functions and macros
- Vectors and packages
- Tagged pointers with type information and garbage collection support

### `heap.zig`
Memory management system implementing a garbage-collected heap for Wisp objects. Manages allocation, object lifecycle, symbol tables, and provides the core runtime environment for program execution.

### `step.zig`
Expression evaluation engine that implements the core interpreter loop. Handles function calls, macro expansion, control flow, and maintains execution context for Wisp programs.

## S-Expression Processing

### `sexp.zig`
Main S-expression module that re-exports parsing, serialization, and pretty-printing functionality.

### `sexp-read.zig`
S-expression parser that converts text input into internal Wisp data structures. Handles Lisp syntax including atoms, lists, quotes, and special forms.

### `sexp-dump.zig`
Serialization module that converts internal Wisp data structures back to textual S-expression format for output and debugging.

### `sexp-prty.zig`
Pretty-printer for S-expressions that formats Wisp code with proper indentation, line breaks, and visual structure for readable output.

## Built-in Functions (Jets)

### `jets.zig`
Coordination module for Wisp's built-in functions ("jets"). Manages the registry of native functions and integrates control, functional, and web-specific operations.

### `jets-ctl.zig`
Control flow jets including conditional expressions, loops, exception handling, and program flow management operations.

### `jets-fun.zig`
Functional programming jets providing arithmetic, list manipulation, string operations, and core computational primitives.

### `jets-web.zig`
Web-specific jets for browser environments, HTTP operations, DOM manipulation, and web API integration.

## Interactive Environment

### `repl.zig`
Read-Eval-Print Loop implementation providing interactive Wisp programming environment. Handles user input, expression evaluation, result display, and maintains session state.

## Persistence and Storage

### `tape.zig`
Serialization system for saving and loading complete Wisp heap states. Enables persistence of program state, core images, and checkpoint/restore functionality.

### `disk.zig`
File system abstraction layer that handles cross-platform file operations, with special support for WASI environments and sandboxed execution.

## Memory Management

### `tidy.zig`
Garbage collection implementation that reclaims unused memory, compacts the heap, and maintains system performance by cleaning up unreferenced objects.

## Utilities

### `util.zig`
General utility functions and helper routines used throughout the Wisp implementation.

### `file.zig`
File I/O operations and abstractions for reading/writing files across different platforms.

### `keys.zig`
Cryptographic key generation and encoding utilities. Implements Z-Base-32 encoding for generating unique identifiers and cryptographic keys.

### `peek.zig`
Debugging and introspection utilities for examining internal Wisp data structures and system state.

## Lisp Source Files

### `lisp/base.wisp`
Core Lisp library defining fundamental macros and functions including `DEFUN`, `DEFMACRO`, `DEFVAR`, and basic language constructs that form the foundation of the Wisp language.

### `lisp/repl.wisp`
REPL-specific functions and utilities for interactive programming, including command parsing, context management, and user interface helpers.

### `lisp/test.wisp`
Test framework and testing utilities for Wisp programs, providing assertion functions and test organization capabilities.

## Generated/Cache Directories

### `.zig-cache/`
Zig compiler cache directory containing intermediate build artifacts and compilation cache files.

### `zig-out/`
Build output directory containing compiled executables, libraries, and other build artifacts generated by the Zig build system.