/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.10.13. */

#ifndef SAB_DELAY_H
#define SAB_DELAY_H

#include "stdint.h"
#define float32_t float

// Effect: delay
typedef struct {
        float32_t mix_f32;
        float32_t time_f32;
        float32_t feedback_f32;
} SAB_delay_tst;


// Process Function for SAB_delay_tst
int SAB_delay_init( SAB_delay_tst* self, float input_f32, float output_f32);

// Process Function for SAB_delay_tst
int SAB_delay_process( SAB_delay_tst* self, float input_f32, float output_f32);



#endif