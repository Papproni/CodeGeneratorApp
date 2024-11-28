/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.11.28. */

#ifndef SAB_OCTAVE_H
#define SAB_OCTAVE_H

#include "sab_intercom.h"
#include "stdint.h"
#define float32_t float

// Effect: octave
typedef struct {
    void (*init)(void*);           // Function pointer to initialize the effect
    int (*process)(void*);
    void (*delete)(void*);
     
    fx_data_tst			intercom_fx_data;
	sab_fx_param_tun 	intercom_parameters_aun[NUM_OF_MAX_PARAMS];

    float32_t param_1_value;
    float32_t param_2_value;
    float32_t param_3_value;
    float32_t param_4_value;
    float32_t param_5_value;
    float32_t param_6_value;
    float32_t param_7_value;
    float32_t param_8_value;
    float32_t param_9_value;
    float32_t param_10_value;
    float32_t param_11_value;
    float32_t param_12_value;
        float32_t octave1_up_vol_f32;
        float32_t octave2_up_vol_f32;
        float32_t octave1_down_vol_f32;
        float32_t octave2_down_vol_f32;
        float32_t normal_vol_f32;
} SAB_octave_tst;


// Process Function for SAB_octave_tst
void SAB_octave_init( SAB_octave_tst* self);

// Process Function for SAB_octave_tst
float32_t SAB_octave_process( SAB_octave_tst* self, float input_f32);

// Process Function for SAB_octave_tst
void SAB_octave_delete( SAB_octave_tst* self);


#endif