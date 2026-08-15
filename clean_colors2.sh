#!/bin/bash
find src/components -type f -name "*.tsx" -exec sed -i \
  -e 's/bg-emerald-600 hover:bg-emerald-700/bg-blue-600 hover:bg-blue-700/g' \
  -e 's/bg-rose-600 hover:bg-rose-700/bg-slate-800 hover:bg-slate-900/g' \
  -e 's/bg-emerald-600/bg-blue-600/g' \
  -e 's/bg-rose-600/bg-slate-800/g' \
  -e 's/text-emerald-600/text-slate-700/g' \
  -e 's/text-emerald-500/text-slate-500/g' \
  -e 's/text-rose-500/text-slate-500/g' \
  -e 's/text-rose-600/text-slate-700/g' \
  -e 's/text-amber-500/text-slate-500/g' \
  -e 's/text-amber-600/text-slate-700/g' \
  -e 's/focus:ring-emerald-500/focus:ring-blue-500/g' \
  -e 's/dark:text-emerald-400/dark:text-slate-300/g' \
  -e 's/dark:text-rose-400/dark:text-slate-300/g' \
  -e 's/dark:text-amber-400/dark:text-slate-300/g' \
  -e 's/bg-emerald-500 text-white/bg-blue-600 text-white/g' \
  -e 's/bg-amber-500 text-white/bg-blue-600 text-white/g' \
  {} +
