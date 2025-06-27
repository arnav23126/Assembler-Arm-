# RISC-V Assembler and Simulator

A Python-based RISC-V assembler and simulator that converts RISC-V assembly code to binary and simulates its execution.

## Project Overview

This project implements a complete RISC-V toolchain consisting of:

- **Assembler**: Converts RISC-V assembly instructions to 32-bit binary machine code
- **Simulator**: Executes the binary machine code and tracks register/memory states

## Files

- [`Assembler.py`](Assembler.py) - RISC-V assembler that converts assembly to binary
- [`Simulator.py`](Simulator.py) - RISC-V processor simulator
- [`members.txt`](members.txt) - Team member identification numbers

## Features

### Assembler ([`Assembler.py`](Assembler.py))
- Supports standard RISC-V instruction types (R, I, S, B, U, J)
- Custom instruction extensions: `mul`, `rst`, `halt`, `rvrs`
- Label processing and resolution
- Error detection and reporting
- Binary output generation

### Supported Instructions
- **R-type**: `add`, `sub`, `sll`, `slt`, `sltu`, `xor`, `srl`, `or`, `and`
- **I-type**: `lw`, `addi`, `sltiu`, `jalr`
- **S-type**: `sw`, `sb`, `sh`, `sd`
- **B-type**: `beq`, `bne`, `blt`, `bge`, `bltu`, `bgeu`
- **U-type**: `lui`, `auipc`
- **J-type**: `jal`
- **Custom**: `mul`, `rst`, `halt`, `rvrs`

### Simulator ([`Simulator.py`](Simulator.py))
- 32 RISC-V registers with proper initialization
- Memory simulation (32 words)
- Instruction execution with state tracking
- Binary arithmetic operations
- Program counter management

## Usage

### Assembler
```bash
python Assembler.py <input_assembly_file> <output_binary_file>
```

### Simulator
```bash
python Simulator.py <input_binary_file> <output_status_file>
```

## Register Set
The simulator implements all 32 RISC-V registers:

- `x0` (zero) - Always zero
- `x1` (ra) - Return address
- `x2` (sp) - Stack pointer (initialized to 256)
- `x3-x31` - General purpose registers

## Memory Layout
- Memory addresses: `0x00010000` to `0x0001007C`
- Word-aligned access (4-byte boundaries)
- 32 memory locations initialized to 0

## Team Members
- 2023098
- 2023126
- 2023017
- 2023236

## Error Handling
The assembler provides comprehensive error detection for:

- Invalid instruction names
- Invalid register names
- Invalid immediate values
- Missing virtual halt instruction

## Output Format
- **Assembler**: Generates 32-bit binary strings
- **Simulator**: Outputs register states and memory contents
