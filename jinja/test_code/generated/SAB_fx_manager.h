/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.09.29. */

#ifndef SAB__H
#define SAB__H


#include "stdint.h"

// Generated effect libs
#include "SAB_delay.h"
#include "SAB_overdrive.h"
#include "SAB_distortion.h"
#include "SAB_octave.h"


// Manager structure: fx_manager
typedef struct {
} SAB_fx_manager_tst;


// Process Function for SAB_fx_manager_tst
int SAB_fx_manager_init( SAB_fx_manager_tst* self, float input_f32, float output_f32);

// Process Function for SAB_fx_manager_tst
int SAB_fx_manager_process( SAB_fx_manager_tst* self, float input_f32, float output_f32);



#endif