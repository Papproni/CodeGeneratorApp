/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.11.11. */

#ifndef SAB_DELAY_H
#define SAB_DELAY_H

#include "sab_intercom.h"
#include "stdint.h"
#define float32_t float

// Effect: delay
typedef struct {
    void (*init)(void*);           // Function pointer to initialize the effect
    int (*process)(void*);
    void (*delete)(void*);
     
    fx_data_tst			intercom_fx_data;
	sab_fx_param_tun 	intercom_parameters_aun[NUM_OF_MAX_PARAMS];
        float32_t mix_f32;
        float32_t time_f32;
        float32_t feedback_f32;
} SAB_delay_tst;


// Process Function for SAB_delay_tst
void SAB_delay_init( SAB_delay_tst* self, float input_f32, float output_f32);

// Process Function for SAB_delay_tst
int SAB_delay_process( SAB_delay_tst* self, float input_f32, float output_f32);



#endif