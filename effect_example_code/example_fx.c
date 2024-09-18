#include "example_fx.h"


void init_TEMPLATE(void* effect) {
    TEMPLATE_effect_tst* self = (TEMPLATE_effect_tst*)effect;
    self->delay_time = 200;
    // init variables, funcs
}

void process_TEMPLATE(void* effect) {
    TEMPLATE_effect_tst* self = (TEMPLATE_effect_tst*)effect;
    // Do effect
}
