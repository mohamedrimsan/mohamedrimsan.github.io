import { readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join, relative } from 'node:path';
import { spawnSync } from 'node:child_process';

const root = fileURLToPath(new URL('../', import.meta.url));

function javascriptFiles(directory) {
  return readdirSync(directory, { withFileTypes: true }).flatMap(entry => {
    const path = join(directory, entry.name);
    return entry.isDirectory()
      ? javascriptFiles(path)
      : /\.(m?js)$/.test(entry.name) ? [path] : [];
  });
}

const files = [...javascriptFiles(join(root, 'assets/js')), ...javascriptFiles(join(root, 'scripts'))];

for (const file of files) {
  const result = spawnSync(process.execPath, ['--check', file], { encoding: 'utf8' });
  if (result.error || result.status !== 0) {
    console.error(`Invalid JavaScript: ${relative(root, file)}`);
    console.error(result.error?.message || result.stderr);
    process.exit(1);
  }
}

console.log(`JavaScript syntax: ${files.length} files passed.`);
