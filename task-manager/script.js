/**
 * Task Manager Application
 * Manages tasks with add, delete, and complete functionality
 * Persists data to localStorage
 */

class TaskManager {
    constructor() {
        this.tasks = this.loadTasks();
        this.currentFilter = 'all';
        this.initializeDOM();
        this.attachEventListeners();
        this.validateInput(); // Initialize validation state
        this.render();
    }

    /**
     * Initialize DOM elements
     */
    initializeDOM() {
        this.taskForm = document.getElementById('taskForm');
        this.taskInput = document.getElementById('taskInput');
        this.taskList = document.getElementById('taskList');
        this.filterButtons = document.querySelectorAll('.filter-btn');
        this.clearCompletedBtn = document.getElementById('clearCompletedBtn');
        this.totalTasksEl = document.getElementById('totalTasks');
        this.completedTasksEl = document.getElementById('completedTasks');
        this.remainingTasksEl = document.getElementById('remainingTasks');
    }

    /**
     * Attach event listeners to DOM elements
     */
    attachEventListeners() {
        // Form submission
        this.taskForm.addEventListener('submit', (e) => {
            e.preventDefault();
            this.addTask();
        });

        // Input validation on keyup
        this.taskInput.addEventListener('input', (e) => {
            this.validateInput();
        });

        // Filter buttons
        this.filterButtons.forEach((btn) => {
            btn.addEventListener('click', (e) => {
                this.filterButtons.forEach((b) => {
                    b.classList.remove('active');
                    b.setAttribute('aria-pressed', 'false');
                });
                e.target.classList.add('active');
                e.target.setAttribute('aria-pressed', 'true');
                this.currentFilter = e.target.dataset.filter;
                this.render();
            });
        });

        // Clear completed button
        this.clearCompletedBtn.addEventListener('click', () => {
            if (this.hasCompletedTasks()) {
                if (confirm('Are you sure you want to delete all completed tasks?')) {
                    this.clearCompleted();
                }
            }
        });
    }

    /**
     * Load tasks from localStorage
     * @returns {Array} Array of task objects
     */
    loadTasks() {
        try {
            const stored = localStorage.getItem('tasks');
            return stored ? JSON.parse(stored) : [];
        } catch (error) {
            console.error('Error loading tasks from localStorage:', error);
            return [];
        }
    }

    /**
     * Save tasks to localStorage
     */
    saveTasks() {
        try {
            localStorage.setItem('tasks', JSON.stringify(this.tasks));
        } catch (error) {
            console.error('Error saving tasks to localStorage:', error);
        }
    }

    /**
     * Add a new task
     */
    addTask() {
        const inputValue = this.taskInput.value.trim();

        // Validation
        if (!inputValue) {
            // Set aria-invalid for accessibility
            this.taskInput.setAttribute('aria-invalid', 'true');
            this.taskInput.focus();
            return;
        }

        // Create task object with trimmed text
        const task = {
            id: this.generateId(),
            text: inputValue, // Already trimmed
            completed: false,
            createdAt: new Date().toISOString(),
        };

        // Add to tasks array
        this.tasks.unshift(task);
        this.saveTasks();

        // Clear input, reset validation state, and re-render
        this.taskInput.value = '';
        this.taskInput.setAttribute('aria-invalid', 'false');
        this.taskInput.focus();
        this.validateInput();
        this.render();
    }

    /**
     * Validate task input field
     * Updates button disabled state and aria-invalid attribute
     */
    validateInput() {
        const inputValue = this.taskInput.value.trim();
        const submitBtn = this.taskForm.querySelector('.btn-primary');
        const isValid = inputValue.length > 0;

        // Update button disabled state
        submitBtn.disabled = !isValid;

        // Update aria-invalid for accessibility
        if (isValid) {
            this.taskInput.removeAttribute('aria-invalid');
        } else {
            this.taskInput.setAttribute('aria-invalid', 'true');
        }
    }

    /**
     * Delete a task by ID
     * @param {string} id Task ID
     */
    deleteTask(id) {
        const taskIndex = this.tasks.findIndex((task) => task.id === id);
        if (taskIndex > -1) {
            this.tasks.splice(taskIndex, 1);
            this.saveTasks();
            this.render();
        }
    }

    /**
     * Toggle task completion status
     * @param {string} id Task ID
     */
    toggleComplete(id) {
        const task = this.tasks.find((task) => task.id === id);
        if (task) {
            task.completed = !task.completed;
            this.saveTasks();
            this.render();
        }
    }

    /**
     * Clear all completed tasks
     */
    clearCompleted() {
        this.tasks = this.tasks.filter((task) => !task.completed);
        this.saveTasks();
        this.render();
    }

    /**
     * Get filtered tasks based on current filter
     * @returns {Array} Filtered tasks array
     */
    getFilteredTasks() {
        switch (this.currentFilter) {
            case 'active':
                return this.tasks.filter((task) => !task.completed);
            case 'completed':
                return this.tasks.filter((task) => task.completed);
            default:
                return this.tasks;
        }
    }

    /**
     * Check if there are completed tasks
     * @returns {boolean}
     */
    hasCompletedTasks() {
        return this.tasks.some((task) => task.completed);
    }

    /**
     * Calculate task statistics
     * @returns {Object} Statistics object
     */
    getStats() {
        const total = this.tasks.length;
        const completed = this.tasks.filter((task) => task.completed).length;
        const remaining = total - completed;

        return { total, completed, remaining };
    }

    /**
     * Format date to readable string
     * @param {string} isoDate ISO date string
     * @returns {string} Formatted date
     */
    formatDate(isoDate) {
        const date = new Date(isoDate);
        const today = new Date();
        const yesterday = new Date(today);
        yesterday.setDate(yesterday.getDate() - 1);

        // Format time
        const timeOptions = { hour: '2-digit', minute: '2-digit' };
        const timeFormatter = new Intl.DateTimeFormat('en-US', timeOptions);

        if (date.toDateString() === today.toDateString()) {
            return `Today at ${timeFormatter.format(date)}`;
        } else if (date.toDateString() === yesterday.toDateString()) {
            return `Yesterday at ${timeFormatter.format(date)}`;
        } else {
            const dateOptions = { month: 'short', day: 'numeric' };
            const dateFormatter = new Intl.DateTimeFormat('en-US', dateOptions);
            return dateFormatter.format(date);
        }
    }

    /**
     * Generate unique ID for tasks
     * @returns {string} Unique ID
     */
    generateId() {
        return `task-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    }

    /**
     * Render the task list
     */
    render() {
        this.renderTasks();
        this.updateStats();
        this.updateClearButton();
    }

    /**
     * Render task list items
     */
    renderTasks() {
        const filteredTasks = this.getFilteredTasks();

        // Clear task list
        this.taskList.innerHTML = '';

        // Show empty state if no tasks
        if (filteredTasks.length === 0) {
            const emptyStateEl = document.createElement('li');
            emptyStateEl.className = 'empty-state';
            emptyStateEl.setAttribute('role', 'listitem');
            emptyStateEl.innerHTML =
                this.currentFilter === 'all'
                    ? '<p>No tasks yet. Add one to get started!</p>'
                    : `<p>No ${this.currentFilter} tasks at the moment.</p>`;
            this.taskList.appendChild(emptyStateEl);
            return;
        }

        // Render each task
        filteredTasks.forEach((task) => {
            const taskEl = this.createTaskElement(task);
            this.taskList.appendChild(taskEl);
        });
    }

    /**
     * Create a task element
     * @param {Object} task Task object
     * @returns {HTMLElement} Task list item element
     */
    createTaskElement(task) {
        const li = document.createElement('li');
        li.className = `task-item ${task.completed ? 'completed' : ''}`;
        li.setAttribute('role', 'listitem');

        li.innerHTML = `
            <input
                type="checkbox"
                class="task-checkbox"
                ${task.completed ? 'checked' : ''}
                aria-label="Toggle completion for: ${this.escapeHtml(task.text)}"
            >
            <div class="task-content">
                <div class="task-text">${this.escapeHtml(task.text)}</div>
                <div class="task-time">${this.formatDate(task.createdAt)}</div>
            </div>
            <div class="task-actions">
                <button
                    class="task-btn task-btn-delete"
                    aria-label="Delete task: ${this.escapeHtml(task.text)}"
                    title="Delete task"
                >
                    🗑️
                </button>
            </div>
        `;

        // Attach event listeners
        const checkbox = li.querySelector('.task-checkbox');
        const deleteBtn = li.querySelector('.task-btn-delete');

        checkbox.addEventListener('change', () => this.toggleComplete(task.id));
        deleteBtn.addEventListener('click', () => this.deleteTask(task.id));

        return li;
    }

    /**
     * Escape HTML special characters to prevent XSS
     * @param {string} text Text to escape
     * @returns {string} Escaped text
     */
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * Update task statistics display
     */
    updateStats() {
        const { total, completed, remaining } = this.getStats();
        this.totalTasksEl.textContent = total;
        this.completedTasksEl.textContent = completed;
        this.remainingTasksEl.textContent = remaining;
    }

    /**
     * Update clear completed button visibility
     */
    updateClearButton() {
        if (this.hasCompletedTasks()) {
            this.clearCompletedBtn.style.display = 'block';
        } else {
            this.clearCompletedBtn.style.display = 'none';
        }
    }
}

/**
 * Initialize the app when DOM is ready
 */
document.addEventListener('DOMContentLoaded', () => {
    new TaskManager();
});
