#ifndef MAX_MACRO_H
#define MAX_MACRO_H

/* Type safety check */
#define MAX_TYPE_CHECK(a, b) \
    ((void)sizeof((a) == (b)))

/* Core MAX implementation (single evaluation safe) */
#define MAX_IMPL(a, b) \
    ({ \
        typeof(a) _a = (a); \
        typeof(b) _b = (b); \
        _a > _b ? _a : _b; \
    })

/* DEBUG VERSION - with tracing */
#ifdef DEBUG

#include <stdio.h>

#define MAX(a, b) \
    ({ \
        MAX_TYPE_CHECK(a, b); \
        typeof(a) _result = MAX_IMPL(a, b); \
        fprintf(stderr, "[DEBUG] MAX called at %s:%d -> (%s=?%lld, %s=?%lld) => %lld\n", \
            __FILE__, __LINE__, \
            #a, (long long)(a), \
            #b, (long long)(b), \
            (long long)_result); \
        _result; \
    })

/* RELEASE VERSION - Optimized: no logging, minimal overhead */
#else

#define MAX(a, b) \
    ( \
        MAX_TYPE_CHECK(a, b), \
        MAX_IMPL(a, b) \
    )

#endif /* DEBUG */

#endif /* MAX_MACRO_H */
