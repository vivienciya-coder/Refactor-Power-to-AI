# Task Manager Web Application

A modern, responsive, and fully accessible task manager web application built with vanilla HTML, CSS, and JavaScript.

## Features

### Core Functionality
- ✅ **Add Tasks** - Create new tasks with a clean, intuitive interface
- ✅ **Mark Complete** - Toggle tasks as completed with a checkbox
- ✅ **Delete Tasks** - Remove individual tasks or clear all completed tasks
- ✅ **Filter View** - View all, active, or completed tasks
- ✅ **Statistics** - Real-time task counters (Total, Completed, Remaining)

### Design & UX
- 🎨 **Modern Styling** - Gradient backgrounds, smooth animations, and transitions
- 📱 **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile devices
- 🌙 **Dark Mode Support** - Automatically adapts to system color scheme preferences
- ✨ **Smooth Animations** - Slide-in effects and hover interactions
- 🎯 **Clean Interface** - Minimalist design with excellent visual hierarchy

### Accessibility
- ♿ **WCAG Compliant** - Meets web content accessibility guidelines
- ⌨️ **Keyboard Navigation** - Fully navigable with keyboard only
- 🔊 **Screen Reader Support** - Proper ARIA labels and semantic HTML
- 👁️ **Focus Indicators** - Clear visual feedback for focused elements
- 🎯 **Semantic HTML** - Uses proper HTML5 semantic elements

### Data Persistence
- 💾 **Local Storage** - Tasks persist across browser sessions
- 🔒 **Safe Storage** - Error handling for storage operations
- 📱 **Device Syncing** - Data saved locally on each device

## File Structure

```
task-manager/
├── index.html      # Semantic HTML markup
├── styles.css      # Modern, responsive CSS styling
├── script.js       # JavaScript functionality
└── README.md       # Documentation
```

## How to Use

### Getting Started
1. Open `index.html` in a web browser
2. Type a task description in the input field
3. Click "Add Task" or press Enter
4. Your task appears in the list below

### Managing Tasks
- **Mark Complete**: Click the checkbox next to a task
- **Delete Task**: Click the 🗑️ trash icon
- **Filter Tasks**: Use the All/Active/Completed buttons to filter your view
- **Clear All Completed**: Click "Clear Completed" to remove all finished tasks at once

### Keyboard Shortcuts
- Enter - Submit form (when focused on input field)
- Tab - Navigate through elements
- Space - Activate buttons or checkboxes

## Technical Details

### HTML Structure
- Semantic elements: `<header>`, `<main>`, `<section>`, `<form>`, `<ul>`
- ARIA labels: `aria-label`, `aria-pressed`, `aria-placeholder`
- Accessible form controls with proper `<label>` associations
- Screen reader only content (`.sr-only` class)

### CSS Architecture
- **CSS Custom Properties**: Organized color, spacing, and typography variables
- **Mobile-First Approach**: Base styles for mobile, enhanced with media queries
- **Responsive Grid**: CSS Grid for stats cards, adapts to screen size
- **Flexible Layout**: Flexbox for component alignment
- **Animations**: Smooth transitions and keyframe animations
- **Dark Mode**: Complete dark mode support with `prefers-color-scheme`
- **Print Styles**: Optimized layout for printing

### JavaScript Features
- **Class-Based Architecture**: `TaskManager` class encapsulates all functionality
- **Event Delegation**: Efficient event handling
- **DOM Manipulation**: Dynamic rendering of task elements
- **Local Storage API**: Persistent data storage
- **Error Handling**: Try-catch blocks for storage operations
- **XSS Prevention**: HTML escaping to prevent injection attacks
- **Internationalization**: Locale-aware date formatting

## Browser Compatibility

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Optimizations

- No external dependencies - pure vanilla JavaScript
- Efficient DOM queries with minimal reflows/repaints
- CSS animations use GPU acceleration (transform/opacity)
- Local storage for instant data persistence
- Minimal CSS file size with organized structure

## Accessibility Features

### Visual
- High contrast ratios (WCAG AA+)
- Color not the only means of information
- Resizable text without loss of functionality
- Focus indicators on all interactive elements

### Interactive
- Proper button and form element semantics
- ARIA labels for icon-only buttons
- Form validation feedback
- Logical tab order

### Experience
- Clear, readable typography
- Sufficient spacing and hit targets (44px minimum)
- Simplified interactions
- Status updates (task counts update in real-time)

## Customization

### Colors
Edit CSS custom properties in `styles.css` (`:root` section):
```css
--color-primary: #6366f1;
--color-success: #10b981;
--color-danger: #ef4444;
```

### Typography
Modify font-family, sizes, and weights in the global styles section.

### Animations
Adjust transition durations in custom properties:
```css
--transition-fast: 150ms ease-in-out;
--transition-base: 250ms ease-in-out;
```

## Future Enhancement Ideas

- 📅 Due dates for tasks
- 🏷️ Categories and tags
- 🔍 Search and filter by text
- 📊 Statistics dashboard
- 🌐 Cloud sync across devices
- 🎨 Theme selector
- ⏰ Reminders and notifications
- 📁 Task organization by projects

## Browser Developer Tools

Open DevTools and test:
- Lighthouse audit for performance, accessibility, and best practices
- Device emulation for responsive design
- Console for any errors
- Application tab to view stored data in localStorage

## License

Free to use, modify, and distribute.

## Support

For issues or improvements, refer to the inline code comments for detailed explanations of functionality.

---

**Built with vanilla HTML, CSS, and JavaScript** 🚀
