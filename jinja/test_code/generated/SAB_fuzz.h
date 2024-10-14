/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.10.13. */

#ifndef SAB_FUZZ_H
#define SAB_FUZZ_H

#include "stdint.h"
#define float32_t float

// Effect: fuzz
typedef struct {
        float32_t sustain_f32;
        float32_t tone_f32;
        float32_t vol_f32;
} SAB_fuzz_tst;


// Process Function for SAB_fuzz_tst
int SAB_fuzz_init( SAB_fuzz_tst* self, float input_f32, float output_f32);

// Process Function for SAB_fuzz_tst
int SAB_fuzz_process( SAB_fuzz_tst* self, float input_f32, float output_f32);



#endif