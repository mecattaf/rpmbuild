%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @marp-team/marp-cli

Name: %{?scl_prefix}nodejs-marp-team-marp-cli
Version: 3.4.0
Release: 1%{?dist}
Summary: A CLI interface for Marp and Marpit based converters
License: MIT
Group: Development/Libraries
URL: https://github.com/marp-team/marp-cli#readme
Source0: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.23.5.tgz
Source1: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.22.20.tgz
Source2: https://registry.npmjs.org/@babel/highlight/-/highlight-7.23.4.tgz
Source3: https://registry.npmjs.org/@marp-team/marp-cli/-/marp-cli-3.4.0.tgz
Source4: https://registry.npmjs.org/@marp-team/marp-core/-/marp-core-3.9.0.tgz
Source5: https://registry.npmjs.org/@marp-team/marpit/-/marpit-2.6.1.tgz
Source6: https://registry.npmjs.org/@marp-team/marpit-svg-polyfill/-/marpit-svg-polyfill-2.1.0.tgz
Source7: https://registry.npmjs.org/@puppeteer/browsers/-/browsers-1.8.0.tgz
Source8: https://registry.npmjs.org/@tootallnate/quickjs-emscripten/-/quickjs-emscripten-0.23.0.tgz
Source9: https://registry.npmjs.org/@types/node/-/node-20.11.23.tgz
Source10: https://registry.npmjs.org/@types/yauzl/-/yauzl-2.10.3.tgz
Source11: https://registry.npmjs.org/accepts/-/accepts-1.3.8.tgz
Source12: https://registry.npmjs.org/agent-base/-/agent-base-7.1.0.tgz
Source13: https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz
Source14: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source15: https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz
Source16: https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz
Source17: https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz
Source18: https://registry.npmjs.org/ast-types/-/ast-types-0.13.4.tgz
Source19: https://registry.npmjs.org/b4a/-/b4a-1.6.6.tgz
Source20: https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz
Source21: https://registry.npmjs.org/basic-ftp/-/basic-ftp-5.0.5.tgz
Source22: https://registry.npmjs.org/batch/-/batch-0.6.1.tgz
Source23: https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.2.0.tgz
Source24: https://registry.npmjs.org/braces/-/braces-3.0.2.tgz
Source25: https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz
Source26: https://registry.npmjs.org/buffer-crc32/-/buffer-crc32-0.2.13.tgz
Source27: https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz
Source28: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source29: https://registry.npmjs.org/chokidar/-/chokidar-3.6.0.tgz
Source30: https://registry.npmjs.org/chromium-bidi/-/chromium-bidi-0.4.32.tgz
Source31: https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz
Source32: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source33: https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz
Source34: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source35: https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz
Source36: https://registry.npmjs.org/color-string/-/color-string-1.9.1.tgz
Source37: https://registry.npmjs.org/commander/-/commander-2.20.3.tgz
Source38: https://registry.npmjs.org/commander/-/commander-8.3.0.tgz
Source39: https://registry.npmjs.org/commander/-/commander-9.2.0.tgz
Source40: https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-8.3.6.tgz
Source41: https://registry.npmjs.org/cross-fetch/-/cross-fetch-4.0.0.tgz
Source42: https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz
Source43: https://registry.npmjs.org/cssfilter/-/cssfilter-0.0.10.tgz
Source44: https://registry.npmjs.org/data-uri-to-buffer/-/data-uri-to-buffer-6.0.2.tgz
Source45: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source46: https://registry.npmjs.org/debug/-/debug-4.3.4.tgz
Source47: https://registry.npmjs.org/degenerator/-/degenerator-5.0.1.tgz
Source48: https://registry.npmjs.org/depd/-/depd-1.1.2.tgz
Source49: https://registry.npmjs.org/devtools-protocol/-/devtools-protocol-0.0.1191157.tgz
Source50: https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz
Source51: https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.4.tgz
Source52: https://registry.npmjs.org/entities/-/entities-3.0.1.tgz
Source53: https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz
Source54: https://registry.npmjs.org/escalade/-/escalade-3.1.2.tgz
Source55: https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz
Source56: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source57: https://registry.npmjs.org/escodegen/-/escodegen-2.1.0.tgz
Source58: https://registry.npmjs.org/esm/-/esm-3.2.25.tgz
Source59: https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz
Source60: https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz
Source61: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source62: https://registry.npmjs.org/extract-zip/-/extract-zip-2.0.1.tgz
Source63: https://registry.npmjs.org/fast-fifo/-/fast-fifo-1.3.2.tgz
Source64: https://registry.npmjs.org/fd-slicer/-/fd-slicer-1.1.0.tgz
Source65: https://registry.npmjs.org/fill-range/-/fill-range-7.0.1.tgz
Source66: https://registry.npmjs.org/fs-extra/-/fs-extra-11.2.0.tgz
Source67: https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz
Source68: https://registry.npmjs.org/get-stream/-/get-stream-5.2.0.tgz
Source69: https://registry.npmjs.org/get-uri/-/get-uri-6.0.3.tgz
Source70: https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz
Source71: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source72: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source73: https://registry.npmjs.org/highlight.js/-/highlight.js-11.8.0.tgz
Source74: https://registry.npmjs.org/http-errors/-/http-errors-1.6.3.tgz
Source75: https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-7.0.2.tgz
Source76: https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-7.0.4.tgz
Source77: https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz
Source78: https://registry.npmjs.org/import-fresh/-/import-fresh-3.3.0.tgz
Source79: https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source80: https://registry.npmjs.org/ip-address/-/ip-address-9.0.5.tgz
Source81: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source82: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.3.2.tgz
Source83: https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz
Source84: https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz
Source85: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz
Source86: https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz
Source87: https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz
Source88: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source89: https://registry.npmjs.org/js-yaml/-/js-yaml-4.1.0.tgz
Source90: https://registry.npmjs.org/jsbn/-/jsbn-1.1.0.tgz
Source91: https://registry.npmjs.org/json-parse-even-better-errors/-/json-parse-even-better-errors-2.3.1.tgz
Source92: https://registry.npmjs.org/jsonfile/-/jsonfile-6.1.0.tgz
Source93: https://registry.npmjs.org/katex/-/katex-0.16.9.tgz
Source94: https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz
Source95: https://registry.npmjs.org/linkify-it/-/linkify-it-4.0.1.tgz
Source96: https://registry.npmjs.org/lodash.kebabcase/-/lodash.kebabcase-4.1.1.tgz
Source97: https://registry.npmjs.org/lru-cache/-/lru-cache-7.18.3.tgz
Source98: https://registry.npmjs.org/markdown-it/-/markdown-it-13.0.2.tgz
Source99: https://registry.npmjs.org/markdown-it-front-matter/-/markdown-it-front-matter-0.2.3.tgz
Source100: https://registry.npmjs.org/mathjax-full/-/mathjax-full-3.2.2.tgz
Source101: https://registry.npmjs.org/mdurl/-/mdurl-1.0.1.tgz
Source102: https://registry.npmjs.org/mhchemparser/-/mhchemparser-4.2.1.tgz
Source103: https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz
Source104: https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz
Source105: https://registry.npmjs.org/mitt/-/mitt-3.0.1.tgz
Source106: https://registry.npmjs.org/mj-context-menu/-/mj-context-menu-0.6.1.tgz
Source107: https://registry.npmjs.org/mkdirp-classic/-/mkdirp-classic-0.5.3.tgz
Source108: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source109: https://registry.npmjs.org/ms/-/ms-2.1.2.tgz
Source110: https://registry.npmjs.org/nanoid/-/nanoid-3.3.7.tgz
Source111: https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz
Source112: https://registry.npmjs.org/netmask/-/netmask-2.0.2.tgz
Source113: https://registry.npmjs.org/node-fetch/-/node-fetch-2.7.0.tgz
Source114: https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz
Source115: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source116: https://registry.npmjs.org/pac-proxy-agent/-/pac-proxy-agent-7.0.1.tgz
Source117: https://registry.npmjs.org/pac-resolver/-/pac-resolver-7.0.1.tgz
Source118: https://registry.npmjs.org/parent-module/-/parent-module-1.0.1.tgz
Source119: https://registry.npmjs.org/parse-json/-/parse-json-5.2.0.tgz
Source120: https://registry.npmjs.org/parseurl/-/parseurl-1.3.3.tgz
Source121: https://registry.npmjs.org/path-type/-/path-type-4.0.0.tgz
Source122: https://registry.npmjs.org/pend/-/pend-1.2.0.tgz
Source123: https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz
Source124: https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz
Source125: https://registry.npmjs.org/postcss/-/postcss-8.4.35.tgz
Source126: https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.0.15.tgz
Source127: https://registry.npmjs.org/progress/-/progress-2.0.3.tgz
Source128: https://registry.npmjs.org/proxy-agent/-/proxy-agent-6.3.1.tgz
Source129: https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-1.1.0.tgz
Source130: https://registry.npmjs.org/pump/-/pump-3.0.0.tgz
Source131: https://registry.npmjs.org/puppeteer-core/-/puppeteer-core-21.4.1.tgz
Source132: https://registry.npmjs.org/queue-tick/-/queue-tick-1.0.1.tgz
Source133: https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz
Source134: https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz
Source135: https://registry.npmjs.org/resolve-from/-/resolve-from-4.0.0.tgz
Source136: https://registry.npmjs.org/serve-index/-/serve-index-1.9.1.tgz
Source137: https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.1.0.tgz
Source138: https://registry.npmjs.org/simple-swizzle/-/simple-swizzle-0.2.2.tgz
Source139: https://registry.npmjs.org/smart-buffer/-/smart-buffer-4.2.0.tgz
Source140: https://registry.npmjs.org/socks/-/socks-2.8.1.tgz
Source141: https://registry.npmjs.org/socks-proxy-agent/-/socks-proxy-agent-8.0.2.tgz
Source142: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source143: https://registry.npmjs.org/source-map-js/-/source-map-js-1.0.2.tgz
Source144: https://registry.npmjs.org/speech-rule-engine/-/speech-rule-engine-4.0.7.tgz
Source145: https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.1.3.tgz
Source146: https://registry.npmjs.org/statuses/-/statuses-1.5.0.tgz
Source147: https://registry.npmjs.org/streamx/-/streamx-2.16.1.tgz
Source148: https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz
Source149: https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz
Source150: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source151: https://registry.npmjs.org/tar-fs/-/tar-fs-3.0.4.tgz
Source152: https://registry.npmjs.org/tar-stream/-/tar-stream-3.1.7.tgz
Source153: https://registry.npmjs.org/through/-/through-2.3.8.tgz
Source154: https://registry.npmjs.org/tmp/-/tmp-0.2.3.tgz
Source155: https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz
Source156: https://registry.npmjs.org/tr46/-/tr46-0.0.3.tgz
Source157: https://registry.npmjs.org/tslib/-/tslib-2.6.2.tgz
Source158: https://registry.npmjs.org/uc.micro/-/uc.micro-1.0.6.tgz
Source159: https://registry.npmjs.org/unbzip2-stream/-/unbzip2-stream-1.4.3.tgz
Source160: https://registry.npmjs.org/undici-types/-/undici-types-5.26.5.tgz
Source161: https://registry.npmjs.org/universalify/-/universalify-2.0.1.tgz
Source162: https://registry.npmjs.org/urlpattern-polyfill/-/urlpattern-polyfill-9.0.0.tgz
Source163: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source164: https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-3.0.1.tgz
Source165: https://registry.npmjs.org/whatwg-url/-/whatwg-url-5.0.0.tgz
Source166: https://registry.npmjs.org/wicked-good-xpath/-/wicked-good-xpath-1.3.0.tgz
Source167: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz
Source168: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source169: https://registry.npmjs.org/ws/-/ws-8.14.2.tgz
Source170: https://registry.npmjs.org/ws/-/ws-8.16.0.tgz
Source171: https://registry.npmjs.org/xmldom-sre/-/xmldom-sre-0.1.31.tgz
Source172: https://registry.npmjs.org/xss/-/xss-1.0.14.tgz
Source173: https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz
Source174: https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz
Source175: https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz
Source176: https://registry.npmjs.org/yauzl/-/yauzl-2.10.0.tgz
Source177: nodejs-marp-team-marp-cli-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/code-frame)) = 7.23.5
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.22.20
Provides: bundled(npm(@babel/highlight)) = 7.23.4
Provides: bundled(npm(@marp-team/marp-cli)) = 3.4.0
Provides: bundled(npm(@marp-team/marp-core)) = 3.9.0
Provides: bundled(npm(@marp-team/marpit)) = 2.6.1
Provides: bundled(npm(@marp-team/marpit-svg-polyfill)) = 2.1.0
Provides: bundled(npm(@puppeteer/browsers)) = 1.8.0
Provides: bundled(npm(@tootallnate/quickjs-emscripten)) = 0.23.0
Provides: bundled(npm(@types/node)) = 20.11.23
Provides: bundled(npm(@types/yauzl)) = 2.10.3
Provides: bundled(npm(accepts)) = 1.3.8
Provides: bundled(npm(agent-base)) = 7.1.0
Provides: bundled(npm(ansi-regex)) = 5.0.1
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(ansi-styles)) = 4.3.0
Provides: bundled(npm(anymatch)) = 3.1.3
Provides: bundled(npm(argparse)) = 2.0.1
Provides: bundled(npm(ast-types)) = 0.13.4
Provides: bundled(npm(b4a)) = 1.6.6
Provides: bundled(npm(base64-js)) = 1.5.1
Provides: bundled(npm(basic-ftp)) = 5.0.5
Provides: bundled(npm(batch)) = 0.6.1
Provides: bundled(npm(binary-extensions)) = 2.2.0
Provides: bundled(npm(braces)) = 3.0.2
Provides: bundled(npm(buffer)) = 5.7.1
Provides: bundled(npm(buffer-crc32)) = 0.2.13
Provides: bundled(npm(callsites)) = 3.1.0
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(chokidar)) = 3.6.0
Provides: bundled(npm(chromium-bidi)) = 0.4.32
Provides: bundled(npm(cliui)) = 8.0.1
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-convert)) = 2.0.1
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(color-name)) = 1.1.4
Provides: bundled(npm(color-string)) = 1.9.1
Provides: bundled(npm(commander)) = 2.20.3
Provides: bundled(npm(commander)) = 8.3.0
Provides: bundled(npm(commander)) = 9.2.0
Provides: bundled(npm(cosmiconfig)) = 8.3.6
Provides: bundled(npm(cross-fetch)) = 4.0.0
Provides: bundled(npm(cssesc)) = 3.0.0
Provides: bundled(npm(cssfilter)) = 0.0.10
Provides: bundled(npm(data-uri-to-buffer)) = 6.0.2
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(debug)) = 4.3.4
Provides: bundled(npm(degenerator)) = 5.0.1
Provides: bundled(npm(depd)) = 1.1.2
Provides: bundled(npm(devtools-protocol)) = 0.0.1191157
Provides: bundled(npm(emoji-regex)) = 8.0.0
Provides: bundled(npm(end-of-stream)) = 1.4.4
Provides: bundled(npm(entities)) = 3.0.1
Provides: bundled(npm(error-ex)) = 1.3.2
Provides: bundled(npm(escalade)) = 3.1.2
Provides: bundled(npm(escape-html)) = 1.0.3
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(escodegen)) = 2.1.0
Provides: bundled(npm(esm)) = 3.2.25
Provides: bundled(npm(esprima)) = 4.0.1
Provides: bundled(npm(estraverse)) = 5.3.0
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(extract-zip)) = 2.0.1
Provides: bundled(npm(fast-fifo)) = 1.3.2
Provides: bundled(npm(fd-slicer)) = 1.1.0
Provides: bundled(npm(fill-range)) = 7.0.1
Provides: bundled(npm(fs-extra)) = 11.2.0
Provides: bundled(npm(get-caller-file)) = 2.0.5
Provides: bundled(npm(get-stream)) = 5.2.0
Provides: bundled(npm(get-uri)) = 6.0.3
Provides: bundled(npm(glob-parent)) = 5.1.2
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(highlight.js)) = 11.8.0
Provides: bundled(npm(http-errors)) = 1.6.3
Provides: bundled(npm(http-proxy-agent)) = 7.0.2
Provides: bundled(npm(https-proxy-agent)) = 7.0.4
Provides: bundled(npm(ieee754)) = 1.2.1
Provides: bundled(npm(import-fresh)) = 3.3.0
Provides: bundled(npm(inherits)) = 2.0.3
Provides: bundled(npm(ip-address)) = 9.0.5
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-arrayish)) = 0.3.2
Provides: bundled(npm(is-binary-path)) = 2.1.0
Provides: bundled(npm(is-extglob)) = 2.1.1
Provides: bundled(npm(is-fullwidth-code-point)) = 3.0.0
Provides: bundled(npm(is-glob)) = 4.0.3
Provides: bundled(npm(is-number)) = 7.0.0
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(js-yaml)) = 4.1.0
Provides: bundled(npm(jsbn)) = 1.1.0
Provides: bundled(npm(json-parse-even-better-errors)) = 2.3.1
Provides: bundled(npm(jsonfile)) = 6.1.0
Provides: bundled(npm(katex)) = 0.16.9
Provides: bundled(npm(lines-and-columns)) = 1.2.4
Provides: bundled(npm(linkify-it)) = 4.0.1
Provides: bundled(npm(lodash.kebabcase)) = 4.1.1
Provides: bundled(npm(lru-cache)) = 7.18.3
Provides: bundled(npm(markdown-it)) = 13.0.2
Provides: bundled(npm(markdown-it-front-matter)) = 0.2.3
Provides: bundled(npm(mathjax-full)) = 3.2.2
Provides: bundled(npm(mdurl)) = 1.0.1
Provides: bundled(npm(mhchemparser)) = 4.2.1
Provides: bundled(npm(mime-db)) = 1.52.0
Provides: bundled(npm(mime-types)) = 2.1.35
Provides: bundled(npm(mitt)) = 3.0.1
Provides: bundled(npm(mj-context-menu)) = 0.6.1
Provides: bundled(npm(mkdirp-classic)) = 0.5.3
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(ms)) = 2.1.2
Provides: bundled(npm(nanoid)) = 3.3.7
Provides: bundled(npm(negotiator)) = 0.6.3
Provides: bundled(npm(netmask)) = 2.0.2
Provides: bundled(npm(node-fetch)) = 2.7.0
Provides: bundled(npm(normalize-path)) = 3.0.0
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(pac-proxy-agent)) = 7.0.1
Provides: bundled(npm(pac-resolver)) = 7.0.1
Provides: bundled(npm(parent-module)) = 1.0.1
Provides: bundled(npm(parse-json)) = 5.2.0
Provides: bundled(npm(parseurl)) = 1.3.3
Provides: bundled(npm(path-type)) = 4.0.0
Provides: bundled(npm(pend)) = 1.2.0
Provides: bundled(npm(picocolors)) = 1.0.0
Provides: bundled(npm(picomatch)) = 2.3.1
Provides: bundled(npm(postcss)) = 8.4.35
Provides: bundled(npm(postcss-selector-parser)) = 6.0.15
Provides: bundled(npm(progress)) = 2.0.3
Provides: bundled(npm(proxy-agent)) = 6.3.1
Provides: bundled(npm(proxy-from-env)) = 1.1.0
Provides: bundled(npm(pump)) = 3.0.0
Provides: bundled(npm(puppeteer-core)) = 21.4.1
Provides: bundled(npm(queue-tick)) = 1.0.1
Provides: bundled(npm(readdirp)) = 3.6.0
Provides: bundled(npm(require-directory)) = 2.1.1
Provides: bundled(npm(resolve-from)) = 4.0.0
Provides: bundled(npm(serve-index)) = 1.9.1
Provides: bundled(npm(setprototypeof)) = 1.1.0
Provides: bundled(npm(simple-swizzle)) = 0.2.2
Provides: bundled(npm(smart-buffer)) = 4.2.0
Provides: bundled(npm(socks)) = 2.8.1
Provides: bundled(npm(socks-proxy-agent)) = 8.0.2
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(source-map-js)) = 1.0.2
Provides: bundled(npm(speech-rule-engine)) = 4.0.7
Provides: bundled(npm(sprintf-js)) = 1.1.3
Provides: bundled(npm(statuses)) = 1.5.0
Provides: bundled(npm(streamx)) = 2.16.1
Provides: bundled(npm(string-width)) = 4.2.3
Provides: bundled(npm(strip-ansi)) = 6.0.1
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(tar-fs)) = 3.0.4
Provides: bundled(npm(tar-stream)) = 3.1.7
Provides: bundled(npm(through)) = 2.3.8
Provides: bundled(npm(tmp)) = 0.2.3
Provides: bundled(npm(to-regex-range)) = 5.0.1
Provides: bundled(npm(tr46)) = 0.0.3
Provides: bundled(npm(tslib)) = 2.6.2
Provides: bundled(npm(uc.micro)) = 1.0.6
Provides: bundled(npm(unbzip2-stream)) = 1.4.3
Provides: bundled(npm(undici-types)) = 5.26.5
Provides: bundled(npm(universalify)) = 2.0.1
Provides: bundled(npm(urlpattern-polyfill)) = 9.0.0
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(webidl-conversions)) = 3.0.1
Provides: bundled(npm(whatwg-url)) = 5.0.0
Provides: bundled(npm(wicked-good-xpath)) = 1.3.0
Provides: bundled(npm(wrap-ansi)) = 7.0.0
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(ws)) = 8.14.2
Provides: bundled(npm(ws)) = 8.16.0
Provides: bundled(npm(xmldom-sre)) = 0.1.31
Provides: bundled(npm(xss)) = 1.0.14
Provides: bundled(npm(y18n)) = 5.0.8
Provides: bundled(npm(yargs)) = 17.7.2
Provides: bundled(npm(yargs-parser)) = 21.1.1
Provides: bundled(npm(yauzl)) = 2.10.0
AutoReq: no
AutoProv: no

%if 0%{?scl:1}
%define npm_cache_dir npm_cache
%else
%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%endif

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 177 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/marp-cli.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/types %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/marp-cli.js
ln -sf %{nodejs_sitelib}/%{npm_name}/marp-cli.js %{buildroot}%{_bindir}/marp

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/marp
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
