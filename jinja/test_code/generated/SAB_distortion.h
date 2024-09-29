/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.09.29. */

#ifndef SAB_DISTORTION_H
#define SAB_DISTORTION_H

#include "stdint.h"
#define float32_t float

// Effect: distortion
typedef struct {
        float32_t gain_f32;
        float32_t tone_f32;
        float32_t presence_f32;
        float32_t sag_f32;
        float32_t bass_f32;
        float32_t mid_f32;
        float32_t treble_f32;
        float32_t volume_f32;
} SAB_distortion_tst;


// Process Function for SAB_distortion_tst
int SAB_distortion_init( SAB_distortion_tst* self, float input_f32, float output_f32);

// Process Function for SAB_distortion_tst
int SAB_distortion_process( SAB_distortion_tst* self, float input_f32, float output_f32);



#endif