#include "stdint.h"


typedef void (*ProcessFunc)();

typedef enum effect_state_en {
    FX_ACTIVE,
    FX_BYPASS
}effect_state_ten;




typedef enum  {
    DELAY,
    OVERDRIVE,
    DISTORTION,
    TREMOLO,
    OCTAVER,
    CHORUS,
    FLANGER,
    VIBRATO,
    REVERB,
    CUSTOM_FX_1,
    CUSTOM_FX_2,
    CUSTOM_FX_3,
    CUSTOM_FX_4,
    CUSTOM_FX_5
}effect_type_tst;


typedef struct color_st{
    uint8_t r;
    uint8_t g;
    uint8_t b;
}color_tst;

// RAW potmeter data coming from DISPLAY
// typedef struct control_st
// {
//     char     name[10];
//     uint16_t min_value_u16;
//     uint16_t max_value_u16;
//     uint16_t default_value_u16;

//     uint16_t value_u16;
// }control_tst;



typedef struct {
    uint32_t time_in_ms;
    float       mix_f32;
    uint32_t element3;
    uint32_t element4;
    uint32_t element5;
    uint32_t element6;
    uint32_t element7;
    uint32_t element8;
    uint32_t element9;
    uint32_t element10;
    uint32_t element11;
    uint32_t element12;
} Struct12Elements;

// Define a union with the struct and a 12-element array of 32-bit integers
typedef union {
    Struct12Elements structData;  // Access via struct elements
    uint32_t arrayData[12];       // Access via array
}controls_tun;




typedef struct{
    char         name[30];
    color_tst    color;
    controls_tun control;
}effect_default_st;

// union base_main
// {
//     /* data */
// };


typedef struct{
    uint32_t time_in_tic;
}var_internal_tst;


typedef struct delays_st{
    effect_default_st defaults;

    void (*process)();
}delays_tst;


typedef struct {
    effect_state_ten state_en;
    ProcessFunc process;
}slot_tst;

#define FX_TERMINATOR 0xFFFFFFF

typedef struct {
    effect_state_ten signal_path[3];
}active_state_tst;

typedef struct {
    active_state_tst signal_path;
    slot_tst effects[3];
}loop_tst;

typedef struct {
    loop_tst loops[4];
}chain_tst;

typedef struct {
    uint32_t major;
    uint32_t minor;
}preset_tst;

typedef struct {
    preset_tst preset_num_st;
    chain_tst chain[10][10];
}effect_chain_tst;