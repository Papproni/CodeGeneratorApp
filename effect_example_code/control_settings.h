#include "stdint.h"
#include "string.h"

#define float32_t float

#define NUM_OF_CONTROL_SLOTS 12
#define MAX_CHAR_LENGTH_FOR_NAME 5

#define SLOT1  1
#define SLOT2  2
#define SLOT3  3
#define SLOT4  4
#define SLOT5  5
#define SLOT6  6
#define SLOT7  7
#define SLOT8  8
#define SLOT9  9
#define SLOT10 10
#define SLOT11 11
#define SLOT12 12


typedef enum pot_charachteristics_en {
    CHAR_LIN,
    CHAR_LOG,
    CHAR_REV_LOG
}pot_charachteristics_ten;

#define NUM_OF_SRC_SLOTS 2

typedef enum control_source_active {
    SRC_PRIME,
    SRC_SECOND
}control_source_ten;

typedef enum control_source_en {
    SRC_POT,
    SRC_EXT_POT,
    SRC_BTN,
    SCR_HW_BTN2_TAP_TEMPO
}control_source_ten;

typedef struct {
    uint32_t time_in_ms;
    float       mix_f32;
    uint32_t _element3;
    uint32_t _element4;
    uint32_t _element5;
    uint32_t _element6;
    uint32_t _element7;
    uint32_t _element8;
    uint32_t _element9;
    uint32_t _element10;
    uint32_t _element11;
    uint32_t _element12;
} Struct12Elements;

// Define a union with the struct and a 12-element array of 32-bit integers
typedef union {
    Struct12Elements params_st;  // Access via struct elements
    uint32_t param_array_au[NUM_OF_CONTROL_SLOTS];       // Access via array
}control_values_tun;

/*
    SLOT1:
*/

typedef struct {
    char* name[NUM_OF_CONTROL_SLOTS][MAX_CHAR_LENGTH_FOR_NAME];

    float32_t min_f32[NUM_OF_CONTROL_SLOTS];
    float32_t max_f32[NUM_OF_CONTROL_SLOTS];
    pot_charachteristics_ten charachteristics_en[NUM_OF_CONTROL_SLOTS];
    control_source_ten control_source_en[NUM_OF_CONTROL_SLOTS][NUM_OF_SRC_SLOTS];
    
    control_values_tun values;

}controls_tst;

void config_control(controls_tst* self, char* name, float32_t min, float32_t max,
                control_source_ten src, pot_charachteristics_ten characteristics, uint8_t slot){
    // Add name for option
    strcpy(self->name[slot][0],name);
    // add min and max value
    self->min_f32[slot] = min;
    self->max_f32[slot] = max;
    // 
    self->control_source_en[slot][SRC_PRIME] = src;
    self->charachteristics_en[slot] = characteristics;

    
}

void test(){
    controls_tst ctrl;

    // SLOT1
    config_control(&ctrl,"VOL", 0,1.6,      SRC_POT,    CHAR_REV_LOG,   SLOT1);
    config_control(&ctrl,"MIX", 0,0.999,    SRC_POT,    CHAR_REV_LOG,   SLOT2);
    config_control(&ctrl,"TIME",1,96000,    SRC_POT,    CHAR_LIN,       SLOT3);
    config_control(&ctrl,"VOL", 0,0.999,    SRC_POT,    CHAR_LIN,       SLOT4);
    config_control(&ctrl,"MOD", 0,1,        SRC_BTN,    CHAR_LIN,       SLOT5); 

    // Delay time can also be used from SRC_HW_BTN1_TAP_TEMPO 

}
