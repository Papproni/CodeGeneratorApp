/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.11.28. */

#ifndef SAB_FX_MANAGER_H
#define SAB_FX_MANAGER_H


#include "stdint.h"
#include "sab_intercom.h"

// Generated effect libs
#include "SAB_delay.h"
#include "SAB_overdrive.h"
#include "SAB_distortion.h"
#include "SAB_octave.h"
#include "SAB_flanger.h"
#include "SAB_chorus.h"
#include "SAB_boost.h"
#include "SAB_pitchshift.h"
#include "SAB_fuzz.h"
#include "SAB_tremolo.h"
#include "SAB_equalizer.h"
#include "SAB_CUSTOM.h"


// Manager structure: fx_manager
typedef struct {
} SAB_fx_manager_tst;


// Process Function for SAB_fx_manager_tst
int SAB_fx_manager_init( SAB_fx_manager_tst* self, float input_f32, float output_f32);

// Process Function for SAB_fx_manager_tst
int SAB_fx_manager_process( SAB_fx_manager_tst* self, float input_f32, float output_f32);

// Enum representing different effect types
typedef enum {
    DELAY,
    OVERDRIVE,
    DISTORTION,
    OCTAVE,
    FLANGER,
    CHORUS,
    BOOST,
    PITCHSHIFT,
    FUZZ,
    TREMOLO,
    EQUALIZER,
    CUSTOM,
} EffectType;

// Struct for a guitar effect with function pointers
typedef struct {
    void (*init)(void*);           // Function pointer to initialize the effect
    int (*process)(void*);         // Function pointer to process the effect
    void (*delete)(void*);
} GuitarEffect;

void init_effect_chain(GuitarEffect** chain, EffectType* fx_chain, int chain_length) {
    for (int i = 0; i < chain_length; ++i) {
        switch (fx_chain[i]) {
        case DELAY:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_delay_tst));
            chain[i]->init = SAB_delay_init;
            chain[i]->process = SAB_delay_process;
            chain[i]->delete  = SAB_delay_delete;
            break;
        case OVERDRIVE:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_overdrive_tst));
            chain[i]->init = SAB_overdrive_init;
            chain[i]->process = SAB_overdrive_process;
            chain[i]->delete  = SAB_overdrive_delete;
            break;
        case DISTORTION:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_distortion_tst));
            chain[i]->init = SAB_distortion_init;
            chain[i]->process = SAB_distortion_process;
            chain[i]->delete  = SAB_distortion_delete;
            break;
        case OCTAVE:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_octave_tst));
            chain[i]->init = SAB_octave_init;
            chain[i]->process = SAB_octave_process;
            chain[i]->delete  = SAB_octave_delete;
            break;
        case FLANGER:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_flanger_tst));
            chain[i]->init = SAB_flanger_init;
            chain[i]->process = SAB_flanger_process;
            chain[i]->delete  = SAB_flanger_delete;
            break;
        case CHORUS:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_chorus_tst));
            chain[i]->init = SAB_chorus_init;
            chain[i]->process = SAB_chorus_process;
            chain[i]->delete  = SAB_chorus_delete;
            break;
        case BOOST:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_boost_tst));
            chain[i]->init = SAB_boost_init;
            chain[i]->process = SAB_boost_process;
            chain[i]->delete  = SAB_boost_delete;
            break;
        case PITCHSHIFT:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_pitchshift_tst));
            chain[i]->init = SAB_pitchshift_init;
            chain[i]->process = SAB_pitchshift_process;
            chain[i]->delete  = SAB_pitchshift_delete;
            break;
        case FUZZ:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_fuzz_tst));
            chain[i]->init = SAB_fuzz_init;
            chain[i]->process = SAB_fuzz_process;
            chain[i]->delete  = SAB_fuzz_delete;
            break;
        case TREMOLO:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_tremolo_tst));
            chain[i]->init = SAB_tremolo_init;
            chain[i]->process = SAB_tremolo_process;
            chain[i]->delete  = SAB_tremolo_delete;
            break;
        case EQUALIZER:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_equalizer_tst));
            chain[i]->init = SAB_equalizer_init;
            chain[i]->process = SAB_equalizer_process;
            chain[i]->delete  = SAB_equalizer_delete;
            break;
        case CUSTOM:
            chain[i] = (GuitarEffect*)malloc(sizeof(SAB_CUSTOM_tst));
            chain[i]->init = SAB_CUSTOM_init;
            chain[i]->process = SAB_CUSTOM_process;
            chain[i]->delete  = SAB_CUSTOM_delete;
            break;
        default:
            printf("Unknown effect type!\n");
            break;
        }
        // Initialize the effect
        chain[i]->init(chain[i]);
    }
}

// Function to process all effects in the chain
void process_effect_chain(GuitarEffect** chain, int chain_length) {
    for (int i = 0; i < chain_length; ++i) {
        chain[i]->process(chain[i]);
    }
}

// Cleanup the effects in the chain
void cleanup_effect_chain(GuitarEffect** chain, int chain_length) {
    for (int i = 0; i < chain_length; ++i) {
        free(chain[i]);  // Free the allocated memory for each effect
    }
}

#endif