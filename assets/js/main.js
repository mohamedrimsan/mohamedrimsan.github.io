// Module scripts run after HTML parsing; each feature ignores pages without its hooks.
import { initNavigation } from './features/navigation.js';
import { initMotion } from './features/motion.js';
import { initFilters } from './features/filters.js';
import { initClipboard } from './features/clipboard.js';
import { initContactForms } from './features/contact-form.js';

initNavigation();
initMotion();
initFilters();
initClipboard();
initContactForms();
