#!/bin/bash
find src/components -type f -name "*.tsx" -exec sed -i \
  -e 's/bg-emerald-[0-9]\{2,3\}\(\/[0-9]\{2\}\)\?/bg-slate-800/g' \
  -e 's/text-emerald-[0-9]\{2,3\}/text-slate-300/g' \
  -e 's/border-emerald-[0-9]\{2,3\}/border-slate-700/g' \
  -e 's/bg-amber-[0-9]\{2,3\}\(\/[0-9]\{2\}\)\?/bg-slate-800/g' \
  -e 's/text-amber-[0-9]\{2,3\}/text-slate-300/g' \
  -e 's/border-amber-[0-9]\{2,3\}/border-slate-700/g' \
  -e 's/bg-rose-[0-9]\{2,3\}\(\/[0-9]\{2\}\)\?/bg-slate-800/g' \
  -e 's/text-rose-[0-9]\{2,3\}/text-slate-300/g' \
  -e 's/border-rose-[0-9]\{2,3\}/border-slate-700/g' \
  {} +
